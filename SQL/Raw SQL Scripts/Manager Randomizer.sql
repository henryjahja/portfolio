-- Randomize Manager
UPDATE users
SET manager_id = floor((RANDOM()* (user_id - 1)) + 1)
WHERE user_id <> 1;

-- Test
SELECT user_id, manager_id
FROM users
WHERE
	manager_id >= user_id -- Not managing themself
	OR manager_id = 0 -- Not out of range
ORDER BY user_id;



-- Randomize Supervisor
UPDATE users
SET supervisor_id = FLOOR(RANDOM() * (user_id - manager_id) + 1) + manager_id - 1
WHERE user_id <> 1;

-- Test
SELECT user_id, supervisor_id, manager_id
FROM users
WHERE
	(manager_id >= user_id -- Not managing themself
	OR supervisor_id >= user_id -- Not supervising themself or supervised by below
	OR manager_id = 0 -- Not out of range
	OR supervisor_id = 0 -- Not out of range
	OR manager_id > supervisor_id -- Supervisor is not above manager
	) and user_id <> 1
ORDER BY user_id;






SELECT user_id
FROM users
WHERE CAST(manager_id AS INT) >= CAST(user_id AS INT)

ALTER TABLE users 
ALTER COLUMN employee_id TYPE integer;
ALTER TABLE users ALTER COLUMN manager_id TYPE integer
USING manager_id::integer;
ALTER TABLE users ALTER COLUMN supervisor_id TYPE integer
USING supervisor_id::integer;

ALTER TABLE users
ALTER COLUMN employee_id TYPE INT 
USING employee_id::integer;



