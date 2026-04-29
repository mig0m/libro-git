<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
	<form method="post" action="pruebaLogin.php">
		<label for="username">Usuario</label>
		<input type="text" name="username" />
		<label for="password">Contraseña</label>
		<input type="text" name="password" />
		<input type="submit" value="Aceptar" />
	</form>
	
	<?php
		if(isset($_POST['username']) && isset($_POST['password']) && $_POST['username'] !="" && $_POST['password'] != ""){
			$servername = "localhost";
			$username = "root";
			$password = "";
			$databaseName = "pruebas_login";
			
			$conn = mysqli_connect($servername, $username, $password, $databaseName);
			
			if (!$conn) {
				die('No pudo conectarse: ' . mysql_error());
			}
			
			$query = "select * from Users where username ='".$_POST['username']."' and password = '".$_POST['password']."';";
			//$query = mysqli_escape_string($conn, $query);
			
			echo '<p>'.$query.'</p>';
			
			if($res = mysqli_query($conn, $query)){
				if(mysqli_num_rows($res)>0){
					while ($row = mysqli_fetch_assoc($res)) {
						echo 'Bienvenido, '.$row['username'].'!';
					}
				}
				else{
					echo '<p style="color:red;">Datos de inicio de sesión incorrectos</p>';
				}
			}
			else{
				echo 'Pasa por aquí';
			}
			
			mysqli_close($conn);
		}
		else if(isset($_POST['fromPerson']) || isset($_POST['fromPerson'])){
			echo '<p style="color:red;">Falta información de login</p>';
		}
		else{
			echo '<p>Inicie sesión.</p>';
		}
	?>

</body>
</html>
