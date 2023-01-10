<?php

 session_start();
 
 if(!isset($_SESSION['udanarejestracja']))
 {
	 header('Location: index.php');
	 exit();
 }else
 {
	 unset($_SESSION['udanarejestracja']);
 }
    //Usuwanie zmiennych pamiętających wartości wpisane do formularza
	if (isset($_SESSION['fr_nick'])) unset($_SESSION['fr_nick']);
	if (isset($_SESSION['fr_haslo1'])) unset($_SESSION['fr_haslo1']);
	if (isset($_SESSION['fr_haslo2'])) unset($_SESSION['fr_haslo2']);
	
	//Usuwanie błędów rejestracji
	if (isset($_SESSION['e_nick'])) unset($_SESSION['e_nick']);
	if (isset($_SESSION['e_haslo'])) unset($_SESSION['e_haslo']);

?>

<!DOCTYPE HTML>
<html lang="pl>
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>strona logowania</title>
  <link href="style.css" type="text/css" rel="stylesheet"/>
</head>
<body>
Dziękujemy za rejestracje. Prosze zalogować się na konto. <br/><br/>
<a href="index.php">Zaloguj się na swoje konto.</a>
<br/><br/>

</body>
</html>