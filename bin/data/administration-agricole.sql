-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 27, 2021 at 11:10 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `administration-agricole`
--

-- --------------------------------------------------------

--
-- Table structure for table `deanships`
--

CREATE TABLE `deanships` (
  `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `H_NUMBER` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `deanships`
--

INSERT INTO `deanships` (`NAME_`, `H_NUMBER`) VALUES
('kljklj', 87546),
('kjklj', 78749);

-- --------------------------------------------------------

--
-- Table structure for table `farmers`
--

CREATE TABLE `farmers` (
  `ID` int(11) NOT NULL,
  `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `LASTNAME` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `PHONENUMBER` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `DEANSHIP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `HEADNUMBERS` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `farmers`
--

INSERT INTO `farmers` (`ID`, `NAME_`, `LASTNAME`, `PHONENUMBER`, `DEANSHIP`, `HEADNUMBERS`) VALUES
(88965, 'zaeaze', 'azeaze', '5', '', 26);

-- --------------------------------------------------------

--
-- Table structure for table `prosecutionoffices`
--

CREATE TABLE `prosecutionoffices` (
  `NAME_` varchar(255) CHARACTER SET utf8 NOT NULL,
  `LASTNAME` varchar(255) CHARACTER SET utf8 NOT NULL,
  `ADDRESS` varchar(255) CHARACTER SET utf8 NOT NULL,
  `PHONENUMBER` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `USER_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `password` longtext CHARACTER SET utf8 DEFAULT NULL,
  `ProsectionOffices` tinyint(1) NOT NULL DEFAULT 0,
  `farmers` tinyint(1) NOT NULL DEFAULT 0,
  `newFarmers` tinyint(1) NOT NULL DEFAULT 0,
  `history` tinyint(1) NOT NULL DEFAULT 0,
  `distribution` tinyint(1) NOT NULL DEFAULT 0,
  `ProsecutionOffices` tinyint(1) NOT NULL DEFAULT 0,
  `changeProsectutionOffices` tinyint(1) NOT NULL DEFAULT 0,
  `change_` tinyint(1) NOT NULL DEFAULT 0,
  `settings` tinyint(1) NOT NULL DEFAULT 0,
  `deanShips` tinyint(1) NOT NULL DEFAULT 0,
  `addNewDeanShip` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`USER_`, `password`, `ProsectionOffices`, `farmers`, `newFarmers`, `history`, `distribution`, `ProsecutionOffices`, `changeProsectutionOffices`, `change_`, `settings`, `deanShips`, `addNewDeanShip`) VALUES
('anwer', '$pbkdf2-sha256$30000$u5eS8v5fq3WOUeo953wvhQ$kp5DSX33dqlPauXJWjWf/yRIM66xwOu5KyjooM0G0/c', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `deanships`
--
ALTER TABLE `deanships`
  ADD UNIQUE KEY `NAME_` (`NAME_`);

--
-- Indexes for table `farmers`
--
ALTER TABLE `farmers`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `ID` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
