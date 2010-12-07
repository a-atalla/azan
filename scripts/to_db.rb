#!/usr/bin/env ruby
# a simple ruby script converts txt files
# from http://www.searchtruth.com/ to a db works with Azan
# Author: Abdelrahman Ghanem <abom.jdev@gmail.com>
# coding: utf-8
require 'sqlite3'
include SQLite3
$KCODE = 'u' if RUBY_VERSION =~ /1.8/

def countries(files)
  files.map do |fname|
    fname = File.basename(fname,'.txt')
    next if fname =~ /index/
    #return an array with country and file
    #country name is optimized for ex: some_country.txt => Some Country
    [fname.scan(/[A-Za-z]+/).map{|m|m.capitalize}.join("\s"),
     fname+'.txt']
    
  end.compact.sort
end

def countries_list(dir)
  list = {}
  #get all txt files data
  Dir.chdir(dir){
    all = countries(Dir['*.txt'])
  
    all.each do |country, file|
      cities = IO.readlines(file).sort
      if list.key?(country)
	list[country].concat(cities)
        list[country].sort! 
      else
	list[country] = cities
      end
    end
  }
  list
end

def to_db
  dir = ARGV[0]
  out_db = ARGV[1]
  
  File.delete(out_db) if File.exists?(out_db)
  
  db = Database.new(out_db)
  #azna db schema
  db.execute("CREATE TABLE azkar (no int auto_increment PRIMARY KEY ,title text,zekr text)")
  db.execute("CREATE TABLE azkarAlmasa (no int auto_increment primary key,zker text)")
  db.execute("CREATE TABLE azkarAlsabah (no int auto_increment primary key,zker text)")
  db.execute("CREATE TABLE citiesTable (cityNO int primary key,countryNO int,cityName varchar(50),state varchar(30),latitude int,longitude int,timeZone int,dayLight int)")
  db.execute("CREATE TABLE countriesTable (countryNO int primary key,countryName varchar(50) )")
  
  # get a hash with all countries/cities
  list = countries_list(dir)
  
  db.transaction
  country_no = 0
  city_no = 0
  
  list.each do |country,city_data|  
    country_no += 1
    
    db.execute("insert into countriesTable values(#{country_no},'#{country}')")
    
    city_data.each do |data|
      
      data.gsub!("'","''")
      data = data.split(',')
      
      next if data.length < 6

      city_no += 1
      city_name = data[0]
      state = data[1][1..-1]
      #add state if found
      unless state.empty?
	city_name += " -- (State: #{state})"
      end
      latitude = data[2].to_f*10000 #azan divide it by 10000
      longitude = data[3].to_f*10000
      zone = data[4].to_f*100 #azan divide it by 100
      daylight = data[5]
      
      #insert data
      
      db.execute("insert into citiesTable values(#{city_no},#{country_no},'#{city_name}','#{state}',#{latitude},#{longitude},#{zone},#{daylight})")
    end
  end
  
  db.commit
  db.close
end

if ARGV.length < 2
  $sterr.puts "Usage: ruby #{__FILE__} [Text files dir] [Outputs Database]"
else
  to_db
end
