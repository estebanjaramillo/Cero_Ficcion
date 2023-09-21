<?php
// Datos de conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "login_db";

// Crear la conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error en la conexión a la base de datos: " . $conn->connect_error);
}

// Obtener los datos del formulario
$usuario = $_POST['usuario'];
$contraseña = $_POST['contraseña'];

// Consulta SQL para verificar las credenciales del usuario
$consulta = "SELECT * FROM usuarios WHERE usuario='$usuario' AND contraseña='$contraseña'";
$resultado = $conn->query($consulta);

// Verificar si se encontró un usuario con las credenciales proporcionadas
if ($resultado->num_rows == 1) {
    // Inicio de sesión exitoso
    echo "Inicio de sesión exitoso. Bienvenido, $usuario!";
} else {
    // Inicio de sesión fallido
    echo "Nombre de usuario o contraseña incorrectos.";
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
<?php
// Datos de conexión a la base de datos
$servidor = "localhost";
$usuario_db = "root";
$contraseña_db = "";
$base_datos = "login_db";

// Conexión a la base de datos
$conn = new mysqli($servidor, $usuario_db, $contraseña_db, $base_datos);

// Verificar la conexión
if ($conn->connect_error) {
  die("Error en la conexión a la base de datos: " . $conn->connect_error);
}

// Obtener los datos del formulario
$usuario = $_POST['usuario'];
$contraseña = $_POST['contraseña'];

// Consulta SQL para verificar las credenciales del usuario
$consulta = "SELECT * FROM usuarios WHERE usuario='$usuario' AND contraseña='$contraseña'";
$resultado = $conn->query($consulta);

// Verificar si se encontró un usuario con las credenciales proporcionadas
if ($resultado->num_rows == 1) {
  // Inicio de sesión exitoso
  echo "Inicio de sesión exitoso. Bienvenido, $usuario!";
} else {
  // Inicio de sesión fallido
  echo "Nombre de usuario o contraseña incorrectos.";
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
