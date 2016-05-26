CREATE TABLE conference (name text, description text, primary key (name));
CREATE TABLE venue (id integer primary key, name text unique, city text, country text, lat numeric(7,5), lon numeric(8,5), unique (city, country, lat, lon));
CREATE TABLE papersubmission(id integer primary key, conference text, year integer, title text, isbn text unique, page integer, venue_id integer, unique (conference, year, isbn), foreign key (conference) references conference (name), foreign key (venue_id) references venue (id));
