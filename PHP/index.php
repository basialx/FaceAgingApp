<?php

 session_start();
 
 if((isset($_SESSION['zalogowany']))&&($_SESSION['zalogowany']==true))
 {
	 header('Location: aplikacja.php');
	 exit();
 }
 
?>

<!DOCTYPE HTML>
<html lang="pl">
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <link href="style.css" type="text/css" rel="stylesheet"/>
  <title>strona logowania</title>
</head>
<body>
<br/><br/>
Witamy! Prosze sie zalogowac lub zarejstrować, aby przejść do aplikacji.<br/><br/>
<a href="rejestracja.php">Rejestracja - załóż konto</a>
<br/><br/>
	<form action="zaloguj.php" method="post">
	
	 Login:<br/><input type="text" name="login"/><br/>
	 Hasło:<br/><input type="password" name="haslo"/><br/><br/>
	 <input type="submit" value="Zaloguj się"/>
	
	</form>

<?php
  if(isset($_SESSION['blad'])) echo $_SESSION['blad'];
?>

</body>
</html>