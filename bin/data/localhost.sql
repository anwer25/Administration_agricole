-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 04, 2021 at 10:47 PM
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
-- Database: `administration_agricole`
--
CREATE DATABASE IF NOT EXISTS `administration_agricole` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `administration_agricole`;

-- --------------------------------------------------------

--
-- Table structure for table `deanships`
--

CREATE TABLE `deanships` (
  `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `H_NUMBER` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `farmers`
--

CREATE TABLE `farmers` (
  `ID` int(11) NOT NULL,
  `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `LASTNAME` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `DEANSHIP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `PHONENUMBER` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `HEADNUMBERS` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `CIN` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `NAME_` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `LASTNAME` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `DEANSHIP` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `ProsectutionOffices` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `NUMBEROFBAGS` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `DATE_` varchar(255) DEFAULT current_timestamp(),
  `TIKETID` int(11) NOT NULL,
  `PRINTID` varchar(255) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `history` tinyint(1) NOT NULL DEFAULT 0,
  `distribution` tinyint(1) NOT NULL DEFAULT 0,
  `settings` tinyint(1) NOT NULL DEFAULT 0,
  `password` longtext CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`TIKETID`),
  ADD UNIQUE KEY `PRINTID` (`PRINTID`);

--
-- Indexes for table `prosecutionoffices`
--
ALTER TABLE `prosecutionoffices`
  ADD UNIQUE KEY `NAME_` (`NAME_`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `USER_` (`USER_`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `TIKETID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
