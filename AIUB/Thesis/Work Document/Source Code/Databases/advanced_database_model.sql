-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 17, 2018 at 06:07 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bangla_scrapper`
--

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Article id',
  `article_title` varchar(500) NOT NULL COMMENT 'Article title',
  `news_string` text NOT NULL COMMENT 'Newspaper article column',
  `source_name_id` int(11) NOT NULL COMMENT 'Corresponding source name id',
  `date_added` date NOT NULL COMMENT 'Article publication date',
  `user_id` int(11) NOT NULL COMMENT 'Which user id updated this information',
  `domain_id` smallint(6) NOT NULL COMMENT 'Article source domain (e.g. sports, movies, politics)',
  `source_link` varchar(500) NOT NULL COMMENT 'Source address',
  `sentence_count` tinyint(4) NOT NULL COMMENT 'No. of sentence in a article',
  PRIMARY KEY (`id`),
  KEY `article_source_name_id_fk` (`source_name_id`),
  KEY `article_user_information_id_fk` (`user_id`),
  KEY `article_domain_id_fk` (`domain_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='Store articles information';

--
-- Dumping data for table `article`
--

INSERT INTO `article` (`id`, `article_title`, `news_string`, `source_name_id`, `date_added`, `user_id`, `domain_id`, `source_link`, `sentence_count`) VALUES
(1, 'Test Article 1', 'আমি ভাত খাই', 1, '2018-07-11', 1, 1, 'Personal', 1),
(2, 'Test Article 2', 'সে স্কুলে যায়', 2, '2018-07-11', 1, 2, 'Personal', 1);

-- --------------------------------------------------------

--
-- Table structure for table `article_line`
--

DROP TABLE IF EXISTS `article_line`;
CREATE TABLE IF NOT EXISTS `article_line` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Article line id',
  `sentence_string` text NOT NULL COMMENT 'Split of article sentence',
  `article_id` int(11) NOT NULL COMMENT 'Corresponding article id',
  `is_visited` tinyint(2) NOT NULL DEFAULT '0' COMMENT 'Checkmark if sentence is shown to user',
  `is_answered` tinyint(2) NOT NULL DEFAULT '0' COMMENT 'Checkmark if sentence is answered by user',
  `is_justified` tinyint(2) NOT NULL DEFAULT '0' COMMENT 'Checkmark if sentence is justified by expert',
  `word_count` tinyint(4) NOT NULL COMMENT 'Count no. of word in a sentence',
  `user_id` int(11) NOT NULL COMMENT 'Which user id last updated this information',
  `date_updated` date NOT NULL COMMENT 'Date of updated entry',
  PRIMARY KEY (`id`),
  KEY `article_line_article_id_fk` (`article_id`),
  KEY `article_line_user_information_id_fk` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='Store individual lines of article';

--
-- Dumping data for table `article_line`
--

INSERT INTO `article_line` (`id`, `sentence_string`, `article_id`, `is_visited`, `is_answered`, `is_justified`, `word_count`, `user_id`, `date_updated`) VALUES
(1, 'আমি ভাত খাই', 1, 0, 0, 0, 3, 1, '2018-07-11'),
(2, 'সে স্কুলে যায়', 2, 0, 0, 0, 3, 1, '2018-07-11');

-- --------------------------------------------------------

--
-- Table structure for table `domain`
--

DROP TABLE IF EXISTS `domain`;
CREATE TABLE IF NOT EXISTS `domain` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT COMMENT 'Domain id',
  `name` varchar(50) NOT NULL COMMENT 'Name of domain(e.g. sports, politics, travel)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='Store domain information';

--
-- Dumping data for table `domain`
--

INSERT INTO `domain` (`id`, `name`) VALUES
(1, 'Test Domain 1'),
(2, 'Test Domain 2');

-- --------------------------------------------------------

--
-- Table structure for table `pos`
--

DROP TABLE IF EXISTS `pos`;
CREATE TABLE IF NOT EXISTS `pos` (
  `id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT 'POS id',
  `name` varchar(50) NOT NULL COMMENT 'POS name',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='Store parts of speech information';

--
-- Dumping data for table `pos`
--

INSERT INTO `pos` (`id`, `name`) VALUES
(1, 'বিশেষ্য'),
(2, 'বিশেষণ'),
(3, 'সর্বনাম'),
(4, 'অব্যয়'),
(5, 'ক্রিয়া');

-- --------------------------------------------------------

--
-- Table structure for table `source_name`
--

DROP TABLE IF EXISTS `source_name`;
CREATE TABLE IF NOT EXISTS `source_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Source name id',
  `name` varchar(100) NOT NULL COMMENT 'Source name',
  `type` varchar(50) NOT NULL COMMENT 'Source type',
  `edition` varchar(20) NOT NULL COMMENT 'Type of edition (e.g. online, print, ebook)',
  `date_added` date NOT NULL COMMENT 'Date of entry',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='Store source names';

--
-- Dumping data for table `source_name`
--

INSERT INTO `source_name` (`id`, `name`, `type`, `edition`, `date_added`) VALUES
(1, 'Test Case 1', 'Verify', 'Binary', '2018-07-11'),
(2, 'Test Case 2', 'Verify', 'Binary', '2018-07-11');

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

DROP TABLE IF EXISTS `user_information`;
CREATE TABLE IF NOT EXISTS `user_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'User id',
  `full_name` varchar(100) NOT NULL COMMENT 'User full name',
  `email` varchar(100) NOT NULL COMMENT 'User email',
  `password` varchar(100) NOT NULL COMMENT 'User password',
  `user_type` int(2) NOT NULL COMMENT 'user type',
  `contribution` int(11) NOT NULL,
  `actual_answer_count` int(11) NOT NULL,
  `created_at` datetime NOT NULL COMMENT 'Date of entry',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='Store user information';

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`id`, `full_name`, `email`, `password`, `user_type`, `contribution`, `actual_answer_count`, `created_at`) VALUES
(1, 'Dipanjan Banik', 'dipanjanbanik@yahoo.com', '01681563110', 0, 0, 0, '2018-07-11 00:00:00'),
(2, 'Mehedi Hassan Sunny', 'contact.mhsunny@gmail.com', '01687276788', 0, 0, 0, '2018-07-11 00:00:00'),
(3, 'Zarin Tasnim', 'zarinmou1@gmail.com', 'ztmou', 0, 0, 0, '2018-07-11 00:00:00'),
(4, 'demo', 'demo@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 2, 0, 0, '2018-07-12 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
CREATE TABLE IF NOT EXISTS `word` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Word id',
  `word_string` varchar(100) NOT NULL COMMENT 'Word ',
  `pos_id` int(11) NOT NULL,
  `article_line_id` int(11) NOT NULL COMMENT 'Corresponding article line id',
  `user_id` int(11) NOT NULL,
  `is_justified` tinyint(2) NOT NULL DEFAULT '0' COMMENT 'Checkmark if word is fully annotated by justifiers',
  `justifier_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `word_article_line_id_fk` (`article_line_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COMMENT='Store article lines word information';

--
-- Dumping data for table `word`
--

INSERT INTO `word` (`id`, `word_string`, `pos_id`, `article_line_id`, `user_id`, `is_justified`, `justifier_id`) VALUES
(1, 'আমি', 0, 1, 0, 1, 0),
(2, 'ভাত', 0, 1, 0, 0, 0),
(3, 'খাই', 0, 1, 0, 0, 0),
(4, 'সে', 0, 2, 0, 0, 0),
(5, 'স্কুলে', 0, 2, 0, 0, 0),
(6, 'যায়', 0, 2, 0, 0, 0),
(7, 'আমি', 5, 1, 0, 0, 0),
(8, 'ভাত', 6, 1, 0, 0, 0),
(9, 'খাই', 6, 1, 0, 0, 0),
(10, 'সে', 1, 2, 0, 0, 0),
(11, 'স্কুলে', 2, 2, 0, 0, 0),
(12, 'যায়', 3, 2, 0, 0, 0),
(13, 'আমি', 1, 1, 0, 0, 0),
(14, 'ভাত', 2, 1, 0, 0, 0),
(15, 'খাই', 3, 1, 0, 0, 0),
(16, 'সে', 1, 2, 0, 0, 0),
(17, 'স্কুলে', 3, 2, 0, 0, 0),
(18, 'যায়', 6, 2, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `word_annotation_justifiers`
--

DROP TABLE IF EXISTS `word_annotation_justifiers`;
CREATE TABLE IF NOT EXISTS `word_annotation_justifiers` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Justifiers id',
  `word_id` int(11) NOT NULL COMMENT 'Corresponding word id',
  `pos_id` tinyint(4) DEFAULT '0' COMMENT 'Corresponding pos id',
  `is_answered` tinyint(2) DEFAULT '0' COMMENT 'Checkmark if word is annotated by jestifiers',
  `user_id` int(11) NOT NULL COMMENT 'Corresponding justifiers user id',
  `date_added` date NOT NULL COMMENT 'Date of entry',
  PRIMARY KEY (`id`),
  KEY `word_annotation_justifiers_word_id_fk` (`word_id`),
  KEY `word_annotation_justifiers_pos_id_fk` (`pos_id`),
  KEY `word_annotation_justifiers_user_information_id_fk` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `word_annotation_justifiers`
--

INSERT INTO `word_annotation_justifiers` (`id`, `word_id`, `pos_id`, `is_answered`, `user_id`, `date_added`) VALUES
(1, 1, 3, 1, 1, '2018-07-11'),
(2, 2, 1, 1, 1, '2018-07-11'),
(3, 3, 5, 1, 1, '2018-07-11'),
(4, 1, 1, 1, 2, '2018-07-11'),
(5, 2, 3, 1, 2, '2018-07-11'),
(6, 3, 5, 1, 2, '2018-07-11'),
(7, 4, 3, 1, 2, '2018-07-11'),
(8, 5, 1, 1, 2, '2018-07-11'),
(9, 6, 5, 1, 2, '2018-07-11');

-- --------------------------------------------------------

--
-- Table structure for table `word_annotation_respondent`
--

DROP TABLE IF EXISTS `word_annotation_respondent`;
CREATE TABLE IF NOT EXISTS `word_annotation_respondent` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Respondent id',
  `word_id` int(11) NOT NULL COMMENT 'Corresponding word id',
  `pos_id` tinyint(4) DEFAULT '0' COMMENT 'Corresponding pos id',
  `is_answered` tinyint(2) DEFAULT '0' COMMENT 'Checkmark if word is annotated by respondent',
  `user_id` int(11) NOT NULL COMMENT 'Corresponding respondent user id',
  `date_added` date NOT NULL COMMENT 'Date of entry',
  PRIMARY KEY (`id`),
  KEY `word_annotation_respondent_word_id_fk` (`word_id`),
  KEY `word_annotation_respondent_pos_id_fk` (`pos_id`),
  KEY `word_annotation_respondent_user_information_id_fk` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `article_domain_id_fk` FOREIGN KEY (`domain_id`) REFERENCES `domain` (`id`),
  ADD CONSTRAINT `article_source_name_id_fk` FOREIGN KEY (`source_name_id`) REFERENCES `source_name` (`id`),
  ADD CONSTRAINT `article_user_information_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`);

--
-- Constraints for table `article_line`
--
ALTER TABLE `article_line`
  ADD CONSTRAINT `article_line_article_id_fk` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  ADD CONSTRAINT `article_line_user_information_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`);

--
-- Constraints for table `word`
--
ALTER TABLE `word`
  ADD CONSTRAINT `word_article_line_id_fk` FOREIGN KEY (`article_line_id`) REFERENCES `article_line` (`id`);

--
-- Constraints for table `word_annotation_justifiers`
--
ALTER TABLE `word_annotation_justifiers`
  ADD CONSTRAINT `word_annotation_justifiers_pos_id_fk` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`id`),
  ADD CONSTRAINT `word_annotation_justifiers_user_information_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`),
  ADD CONSTRAINT `word_annotation_justifiers_word_id_fk` FOREIGN KEY (`word_id`) REFERENCES `word` (`id`);

--
-- Constraints for table `word_annotation_respondent`
--
ALTER TABLE `word_annotation_respondent`
  ADD CONSTRAINT `word_annotation_respondent_pos_id_fk` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`id`),
  ADD CONSTRAINT `word_annotation_respondent_user_information_id_fk` FOREIGN KEY (`user_id`) REFERENCES `user_information` (`id`),
  ADD CONSTRAINT `word_annotation_respondent_word_id_fk` FOREIGN KEY (`word_id`) REFERENCES `word` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
