create database if not exists cshelper;
use cshelper;
drop table if exists Users;
drop table if exists UserRoles;
drop table if exists OutputVariables;
drop table if exists InputVariables;
drop table if exists AllVariables;
drop table if exists TrainingQuestions;
drop table if exists ExternalDBImports;
drop table if exists ExternalDBConnections;
drop table if exists Categories;
create table Categories (
  category varchar(256),
  primary key (category)
);
create table ExternalDBConnections (
  externconnid serial,
  primary key (externconnid)
);
create table ExternalDBImports (
  externimportid serial,
  conn bigint unsigned not null,
  inputcolumn varchar(128) not null,
  outputcolumn varchar(128) not null,
  category varchar(256) not null,
  unique key (conn, inputcolumn, outputcolumn, category),
  primary key (externimportid),
  foreign key (category) references Categories(category) on update cascade on delete cascade,
  foreign key (conn) references ExternalDBConnections(externconnid) on update cascade on delete cascade
);
create table TrainingQuestions (
  questionid serial,
  question varchar(512) not null,
  cat varchar(128) not null,
  slot varchar(128) not null,
  label varchar(128) not null,
  unique key (question, cat),
  primary key (questionid),
  foreign key (cat) references Categories(category) on update cascade on delete cascade
);
create table AllVariables (
  variable varchar(128),
  fromDB bigint unsigned default null,
  primary key (variable),
  foreign key (fromDB) references ExternalDBImports(externimportid) on update set null on delete set null
);
create table InputVariables (
  inputid serial,
  var varchar(128) not null,
  incat varchar(512) not null,
  primary key (inputid),
  unique key (var, incat),
  foreign key (var) references AllVariables(variable) on update cascade on delete cascade,
  foreign key (incat) references Categories(category) on update cascade on delete cascade
);
create table OutputVariables (
  outvar varchar(128),
  inid bigint unsigned,
  primary key (outvar, inid),
  foreign key (outvar) references AllVariables(variable) on update cascade on delete cascade,
  foreign key (inid) references InputVariables(inputid) on update cascade on delete cascade
);
create table UserRoles (
  rolename varchar(128),
  primary key (rolename)
);
create table Users (
  userid serial,
  username varchar(128) not null unique,
  userrole varchar(128) not null,
  primary key (userid),
  foreign key (userrole) references UserRoles(rolename) on update cascade on delete cascade
);
create table ImportantDates (
  important_event varchar(128) not null unique,
  event_date varchar(128) not null,
  primary key (important_event)
);