SELECT
	u.username,
	p.likes,
	p.content_type
FROM users u
JOIN posts p
	ON u.user_id=p.user_id
WHERE p.content_type = 'Photo';
