CREATE TABLE IF NOT EXISTS `scoretable` 
(
    `user_id` FLOAT NOT NULL,
    `engagement_score` FLOAT NOT NULL,
    `experience_score` FLOAT NOT NULL,
    `satisfaction_score` FLOAT DEFAULT NULL,
    #'user_id': 'FLOAT NOT NULL',
    #'engagement_score': 'INT NOT NULL',
    #'experience_score': 'INT NOT NULL',
    #'satisfaction_score': 'INT DEFAULT NULL',
    PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
