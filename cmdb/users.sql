create table users (
    id int primary key  auto_increment,
    name varchar(50),
    age int default 18,
    gender boolean not null default 0,
    tel varchar(20) not null default '',
    pwd varchar(256)
);


insert into users (name, age, gender, tel, pwd) values ('Jack', 29, 1, '987', 'abc.123');
insert into users (name, age, gender, tel, pwd) values ('Rose', 19, 0, '657', 'abc.123');
