DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id int PRIMARY KEY,
	username varchar(50),
	email varchar(100),
	first_name varchar(50)
);

CREATE TABLE posts (
	post_id int PRIMARY KEY,
	user_id int,
	content_type varchar(50),
	post_date date,
	likes int,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users(user_id, username, email, first_name) VALUES
(1, 'alex123', '123alex@gmail.com', 'Alex'),
(2, 'johntheman', 'hellojohn@outlook.com', 'John'),
(3, 'hooper_990', 'hooper990@gmail.com', 'Patrick'),
(4, 'coo1guy', 'coo1guy1@gmail.com', 'Cooper'),
(5, 'UVAROCKS_703', 'uvaalum703@gmail.com', 'James'),
(6, 'wju9ag', 'wju9ag@virginia.edu', 'Daniel'),
(7, 'idk_idk6', 'daveidk@gmail.com', 'Dave'),
(8, 'bchu412', 'brandonchu@gmail.com', 'Brandon'),
(9, 'sarahyy', 'sarahyy11@gmail.com', 'Sarah'),
(10, 'himorgan', 'morgan23@gmail.com', 'Morgan');

INSERT INTO posts(post_id, user_id, content_type, post_date, likes) VALUES
(1, 1, 'Video', '2026-10-20', 1002),
(2, 4, 'Photo', '2025-02-02' , 11),
(3, 2, 'Reel', '2026-07-09', 924032),
(4, 3, 'Photo', '2025-12-29', 864),
(5, 9, 'Photo', '2026-05-31', 233),
(6, 10, 'Video', '2025-09-09', 6720),
(7, 5, 'Reel', '2026-04-01', 3),
(8, 7, 'Reel', '2026-01-25', 4593022),
(9, 8, 'Photo', '2025-08-03', 5349),
(10, 8, 'Photo', '2026-10-11', 3021);


