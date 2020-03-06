create database if not exists csdepartmentbot;
use csdepartmentbot;
drop table if exists VariableCategories;
drop table if exists AllVariables;
drop table if exists TrainingQuestions;
drop table if exists Categories;
create user if not exists 'cshelperbot'@'localhost' identified by '/*Q+:esb}y~KQ/FLt%_wb(1/T0wI-K&%jeZh<efyC)J#LhMK.a';
grant select, insert, update, delete on csdepartmentbot.* to 'cshelperbot'@'localhost';
create table Categories (
  categoryid bigint auto_increment,
  primarycategory varchar(100) not null,
  secondarycategory varchar(100) not null,
  primary key (categoryid),
  unique key (primarycategory, secondarycategory)
);
create table TrainingQuestions (
  questionid bigint auto_increment,
  question varchar(1024) not null,
  category bigint not null,
  primary key (questionid),
  foreign key (category) references Categories(categoryid) on update cascade on delete cascade
);
create table AllVariables (
  variableid bigint auto_increment,
  variable varchar(1024) not null,
  primary key (variableid)
);
create table VariableCategories (
  vid bigint,
  cid bigint,
  reltype varchar(6) check (reltype in ("input", "output")),
  primary key (vid, cid, reltype),
  foreign key (vid) references AllVariables(variableid) on update cascade on delete cascade,
  foreign key (cid) references Categories(categoryid) on update cascade on delete cascade
);