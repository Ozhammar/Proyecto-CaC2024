-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-07-2024 a las 22:35:11
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `stock_cac2024`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` smallint(6) NOT NULL COMMENT 'ID UNICO DE PRODUCTO',
  `nombre` varchar(255) NOT NULL COMMENT 'NOMBRE DEL PRODUCTO',
  `categoria` varchar(50) NOT NULL COMMENT 'CATEGORIA DEL PRODUCTO',
  `precio` mediumint(9) NOT NULL COMMENT 'PRECIO DEL PRODUCTO',
  `cantidad` mediumint(9) NOT NULL COMMENT 'PRECIO UNITARIO',
  `imagen` varchar(5000) NOT NULL COMMENT 'IMAGEN DEL PRODUCTO'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `categoria`, `precio`, `cantidad`, `imagen`) VALUES
(47, 'Cooler Master COSMOS C700P Black Edition', 'GABINETE', 250000, 5, '2024174411183007Gabinete-Cooler-Master-COSMOS-C700P-Black-Edition-RGB-E-ATX-3x14cm-Templado-+-Controladora-RGB.png'),
(48, 'Cooler Master H500P', 'GABINETE', 150000, 2, '2024174452092957Gabinete-Cooler-Master-MasterCase-H500P-Mesh-White-ARGB-2x20cm-1x14cm.png'),
(49, 'Corsair Crystal 680X', 'GABINETE', 180000, 3, '2024174536469647Gabinete-Corsair-Crystal-680X-RGB-Tempered-Glass-Smart-Black-3x120mm.png'),
(50, 'i3', 'MICRO_INTEL', 200000, 3, '2024174703692317i3.png'),
(51, 'i5', 'MICRO_INTEL', 350000, 6, '2024174722227044i5.jpg'),
(52, 'i7', 'MICRO_INTEL', 650000, 9, '2024174744075008i7.jpg'),
(53, 'i9', 'MICRO_INTEL', 990000, 2, '2024174800385576i9.jpg'),
(54, 'Rysen 3', 'MICRO_AMD', 100000, 3, '2024174928347939ryzen3.png'),
(55, 'Ryzen 5', 'MICRO_AMD', 250000, 6, '2024194540873756ryzen5.png'),
(56, 'Ryzen 7', 'MICRO_AMD', 450000, 7, '2024194602503561ryzen7.jpg'),
(57, 'Ryzen 9', 'MICRO_AMD', 750000, 4, '2024194626611054ryzen9.png'),
(58, 'Corsair Vengeance LPX Black 8GB 3200Mhz', 'DDR4', 35000, 11, '2024194814408910Memoria-RAM-Corsair-8GB-DDR4-3200Mhz-Vengeance-LPX-Black.jpg'),
(59, 'Corsair Vengeance RGB 8GB DDR4 3200Mhz', 'DDR4', 45000, 7, '2024194902601539Memoria-RAM-Corsair-8GB-DDR4-3200Mhz-Vengeance-RGB-RS.png'),
(60, 'Corsair Vengeance LPX Black 2x8Gb DDR4 3200Mhz', 'DDR4', 70000, 32, '2024195026167886Memoria-RAM-Corsair-16Gb-2x8Gb-DDR4-3200Mhz-Vengeance-LPX-Black.jpg'),
(61, 'Corsair Vengeance 16Gb DDR5 5200Mhz', 'DDR5', 80500, 44, '2024195115638190Memoria-RAM-Corsair-16Gb-DDR5-5200Mhz-Vengeance.png'),
(62, 'Corsair Vengeance RGB Black 2x16Gb DDR5 5200Mhz', 'DDR5', 185000, 2, '2024195210839280Memoria-RAM-Corsair-32Gb-2x16G-DDR5-5200Mhz-Vengeance-RGB-Black.png'),
(63, 'ASUS ROG STRIX Z790 A-GAMING WIFI LGA1700', 'MOTHER_INTEL', 750000, 3, '2024195521399696Mother-ASUS-ROG-STRIX-Z790-A-GAMING-WIFI-12-13-14va-Gen-LGA1700.png'),
(64, 'ASUS TUF GAMING B760 PLUS WIFI LGA1700', 'MOTHER_INTEL', 650000, 6, '2024195602292171Mother-ASUS-TUF-GAMING-B760-PLUS-WIFI-12va13va-Gen-LGA1700.png'),
(65, 'ASUS ROG STRIX B450 F-GAMING AM4', 'MOTHER_AMD', 850000, 6, '2024195649614225Mother-ASUS-ROG-STRIX-B450-F-GAMING-II-USB3.1-M2-AM4.jpg'),
(66, 'ASUS ROG STRIX X670E E-GAMING AM5', 'MOTHER_AMD', 750000, 13, '2024195726903354Mother-ASUS-ROG-STRIX-X670E-E-GAMING-WIFI-AM5.png'),
(67, 'MSI MAG B650 TOMAHAWK AM5', 'MOTHER_AMD', 550000, 3, '2024195802606203Mother-MSI-MAG-B650-TOMAHAWK-WIFI-AM5.png'),
(68, 'WD Blue 1TB SATA3', 'HDD', 200000, 11, '2024195927967416Disco-Rigido-PC-1Tb-WD-Blue-SATA3.jpg'),
(69, 'WD Blue 2TB SATA3', 'HDD', 275000, 6, '2024200004835730Disco-Rígido-PC-2Tb-WD-Blue-SATA3.jpg'),
(70, 'WD Blue 4TB SATA3', 'HDD', 485339, 2, '2024200031462235Disco-Rígido-PC-4Tb-WD-Blue-SATA3.jpg'),
(71, 'Kingston 240GB SATA3', 'SSD', 130000, 4, '2024200121460139Disco-SSD-Kingston-240GB-A400-SATA3.png'),
(72, 'Kingston 480GB SATA3', 'SSD', 245000, 5, '2024200137279913Disco-SSD-Kingston-480GB-A400-SATA3.png'),
(73, 'Kingston 960GB SATA3', 'SSD', 222000, 3, '2024200156012259Disco-SSD-Kingston-960GB-A400-SATA3.png'),
(74, 'WD Blue 500Gb SN570 NVME', 'SSDM2', 125000, 4, '2024200240732979Disco-SSD-M2-WD-Blue-500Gb-SN570-NVME.png'),
(75, 'WD Blue 1Tb SN570 NVME', 'SSDM2', 234000, 5, '2024200259987318Disco-SSD-M2-WD-Blue-1Tb-SN570-NVME.jpg'),
(76, 'WD Black 1Tb SN770 ', 'SSDM2', 350000, 1, '2024200330656916Disco-SSD-M2-WD-Black-1Tb-SN770-5000MB.jpg'),
(77, 'Alienware X15 Intel I7 11800H 16GBDDR4 RTX3070 8Gb SSD512Gb', 'NOTEBOOK', 1850000, 1, '2024200513260399Notebook-Alienware-X15-R1-Intel-Core-I7-11800H-16GB-DDR4-RTX-3070-8Gb-512Gb.png'),
(78, 'ASUS TUF FX517ZM Intel I7 12650H 16GBDDR5 RTX 4070 8gb', 'NOTEBOOK', 2450000, 4, '2024200616700169Notebook-ASUS-TUF-Gaming-FX517ZM-Intel-Core-I7-12650H-16GB-DDR5-RTX-4070-8gb.png'),
(79, 'Cooler Master - MasterAir MA620M', 'REFRIGERACION_AIRE', 102000, 3, '2024200906521563Cooler-CPU-Cooler-Master-MasterAir-MA620M-ARGB-Intel-AMD.png'),
(80, 'Cooler Master - MasterAir MA610P', 'REFRIGERACION_AIRE', 55000, 6, '2024200936727588Cooler-CPU-Cooler-Master-MasterAir-MA610P-ARGB-Edition.png'),
(81, 'Thermaltake TH360 ARGB 360mm Black', 'REFRIGERACION_WATER', 105000, 7, '2024201016226858Cooler-CPU-Water-Cooling-Thermaltake-TH360-ARGB-Sync-AIO-360mm-Black-Intel-AMD.png'),
(82, 'Thermaltake TH360 ARGB 360mm', 'REFRIGERACION_WATER', 275000, 3, '2024201053483029Cooler-CPU-Water-Cooling-Thermaltake-TH360-ARGB-Sync-AIO-360mm-Black-Intel-AMD.png'),
(83, 'Corsair RM850X 850W - Full Modular 80Plus Gold', 'GOLD', 85000, 4, '2024201234258690Fuente-Corsair-RM850X-850W-Full-Modular-80-Plus-Gold.png'),
(84, 'EVGA 850W GQ 80Plus Gold - Semi Modular', 'GOLD', 99000, 7, '2024201310257439Fuente-EVGA-850W-GQ-80-Plus-Gold-Semi-Modular.jpg'),
(85, 'Corsair CV650 650W 80Plus Bronze', 'BRONZE', 65000, 3, '2024201338521769Fuente-Corsair-CV650-650W-80-Plus-Bronze.png'),
(86, 'Corsair CV750 750W 80Plus Bronze', 'BRONZE', 103000, 10, '2024201418384676Fuente-Corsair-CV750-750W-80-Plus-Bronze.png'),
(87, 'Palit GeForce RTX 4080 16GB GDDR6X', 'GPU_NVIDIA', 1250357, 4, '2024201558874204Placa-de-Video-Palit-NVIDIA-GeForce-RTX-4080-GAME-ROCK-OC-16GB-GDDR6X.png'),
(88, 'MSI GeForce RTX 4070SUPER Ventus 3X OC 12Gb GDDR6', 'GPU_NVIDIA', 985000, 9, '2024201649458330Placa-de-Video-MSI-NVIDIA-GeForce-RTX-4070-SUPER-Ventus-3X-OC-12Gb-GDDR6X.png'),
(89, 'MSI Radeon RX 6900XT GAMING-Z 16Gb-GDDR6', 'GPU_AMD', 1785000, 7, '2024201742514853Placa-de-Video-MSI-Radeon-RX-6900-XT-GAMING-Z-TRIO-16Gb-GDDR6.jpg'),
(90, 'MSI Radeon RX 7600Mech 2XOC 8Gb GDDR6', 'GPU_AMD', 2750987, 2, '2024201838376704Placa-de-Video-MSI-Radeon-RX-7600-Mech-2X-OC-8Gb-GDDR6.png'),
(91, 'Threadripper', 'MICRO_AMD', 5000000, 1, '2024173300227289Threadripper 2970wx.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `usuario` varchar(11) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `apellido` varchar(55) NOT NULL,
  `email` varchar(55) NOT NULL,
  `password` int(10) NOT NULL,
  `password_conf` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `usuario`, `nombre`, `apellido`, `email`, `password`, `password_conf`) VALUES
(1, '1', 'Gabriel', 'Aballay', 'gabrielaballay99@gmal.com', 1234, 1234),
(5, 'LPovolo', 'Lucas Omar', 'Povolo', 'lucas.povolo1@gmail.com', 456789, 456789);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` smallint(6) NOT NULL AUTO_INCREMENT COMMENT 'ID UNICO DE PRODUCTO', AUTO_INCREMENT=92;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
