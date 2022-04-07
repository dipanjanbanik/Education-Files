-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2018 at 07:39 AM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `random_dataset`
--

-- --------------------------------------------------------

--
-- Table structure for table `article_sentences`
--

CREATE TABLE `article_sentences` (
  `id` int(11) NOT NULL COMMENT 'Article sentence id',
  `sentence_string` text NOT NULL COMMENT 'Random article sentence',
  `source_link` varchar(500) NOT NULL COMMENT 'Source address',
  `word_count` tinyint(4) NOT NULL COMMENT 'Count no. of word in a sentence'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pos`
--

CREATE TABLE `pos` (
  `id` tinyint(4) NOT NULL COMMENT 'POS id',
  `bengali_name` varchar(50) NOT NULL COMMENT 'Bengali POS name',
  `english_name` varchar(50) NOT NULL COMMENT 'English POS name'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pos`
--

INSERT INTO `pos` (`id`, `bengali_name`, `english_name`) VALUES
(1, 'বিশেষ্য', 'Noun'),
(2, 'বিশেষণ', 'Adjective'),
(3, 'সর্বনাম', 'Pronoun'),
(4, 'অব্যয়', 'Preposition'),
(5, 'ক্রিয়া', 'Verb'),
(6, 'উত্তর জানা নেই', 'No answer');

-- --------------------------------------------------------

--
-- Table structure for table `word`
--

CREATE TABLE `word` (
  `id` int(11) NOT NULL COMMENT 'Word id',
  `word_string` varchar(100) NOT NULL COMMENT 'Word text',
  `article_sentence_id` int(11) NOT NULL COMMENT 'Corresponding article sentence id',
  `pos_id` tinyint(4) NOT NULL DEFAULT '6' COMMENT 'Corresponding pos id',
  `tag` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Custom tags'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `article_sentences`
--
ALTER TABLE `article_sentences`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pos`
--
ALTER TABLE `pos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `word`
--
ALTER TABLE `word`
  ADD PRIMARY KEY (`id`),
  ADD KEY `word_article_sentences_id_fk` (`article_sentence_id`),
  ADD KEY `word_pos_id_fk` (`pos_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `article_sentences`
--
ALTER TABLE `article_sentences`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Article sentence id';

--
-- AUTO_INCREMENT for table `pos`
--
ALTER TABLE `pos`
  MODIFY `id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT 'POS id', AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `word`
--
ALTER TABLE `word`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Word id';

--
-- Constraints for dumped tables
--

--
-- Constraints for table `word`
--
ALTER TABLE `word`
  ADD CONSTRAINT `word_article_sentences_id_fk` FOREIGN KEY (`article_sentence_id`) REFERENCES `article_sentences` (`id`),
  ADD CONSTRAINT `word_pos_id_fk` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
