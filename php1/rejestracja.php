<?php

 session_start();
 
 if(isset($_POST['nick']))
 {
	 $wszystko_OK=true;
	 $nick=$_POST['nick']; 
	
	if((strlen($nick)<3) || (strlen($nick)>20))
	{
		$wszystko_OK=false;
		$_SESSION['e_nick']="nick musi miec 3 - 20 znakow";
	}
	
	if (ctype_alnum($nick)==false)
	{
		$wszystko_OK=false;
		$_SESSION['e_nick']="Nick może składać się tylko z liter i cyfr (bez polskich znaków)";
	}
	
	$haslo1 = $_POST['haslo1'];
	$haslo2 = $_POST['haslo2'];
		
	if ((strlen($haslo1)<8) || (strlen($haslo1)>20))
	{
		$wszystko_OK=false;
		$_SESSION['e_haslo']="Hasło musi posiadać 8 - 20 znaków";
	}
		
	if ($haslo1!=$haslo2)
	{
		$wszystko_OK=false;
		$_SESSION['e_haslo']="Podane hasła nie są identyczne!";
	}	

	$haslo_hash = password_hash($haslo1, PASSWORD_DEFAULT);		
	require_once"connect.php";
	mysqli_report(MYSQLI_REPORT_STRICT);
	try
	{
		$polaczenie=new mysqli($host, $db_user, $db_password, $db_name);
		if($polaczenie->connect_errno!=0)
	    {
		  throw new Exception(mysqli_connect_errno());
	    }else
		{
			$rezultat = $polaczenie->query("SELECT id FROM uzytkownicy WHERE user='$nick'");
				
			if (!$rezultat) throw new Exception($polaczenie->error);
				
			$ile_takich_nickow = $rezultat->num_rows;
			if($ile_takich_nickow>0)
			{
				$wszystko_OK=false;
				$_SESSION['e_nick']="Istnieje już gracz o takim nicku. Wybierz inny.";
			}
		    if($wszystko_OK==true)
		    {
			    if ($polaczenie->query("INSERT INTO uzytkownicy VALUES (NULL, '$nick', '$haslo_hash')"))
				{
				    $_SESSION['udanarejestracja']=true;
					header('Location: witamy.php');
					}
					else
					{
						throw new Exception($polaczenie->error);
					}
	         	}
			$polaczenie->close();
		}
	}
	catch(Exception $e)
		{
			echo '<span style="color:red;">Błąd serwera! Przepraszamy za niedogodności i prosimy o rejestrację w innym terminie!</span>';
			echo '<br />Informacja developerska: '.$e;
		}
 }
 
?>

<!DOCTYPE HTML>
<html lang="pl">
<head>
  <meta charset="tf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
  <title>Rejstracja - nowe konto</title>
  <link href="style.css" type="text/css" rel="stylesheet"/>
  <style>
   .error
   {
	   color:red;
	   margin-top:10px;
	   margin-bottom:10px;
   }
  </style>
</head>
<body>
<br/><br/>
  <form method="post">
  
    Nickname: <br/><input type="text" name="nick"/><br/>
	<?php
	 if(isset($_SESSION['e_nick']))
	 {
		 echo '<div class="error">'.$_SESSION['e_nick'].'</div>';
		 unset($_SESSION['e_nick']);
	 }
	?>
	
	Podaj hasło: <br/><input type="password" name="haslo1"/><br/>
	<?php
	 if(isset($_SESSION['e_haslo']))
	 {
		 echo '<div class="error">'.$_SESSION['e_haslo'].'</div>';
		 unset($_SESSION['e_haslo']);
	 }
	?>
	Powtórz hasło: <br/><input type="password" name="haslo2"/><br/>
	<br/>
	<input type="submit"value="Zarejestruj się"/>
	
  </form>

</body>
</html>