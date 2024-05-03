<?php
require_once 'db.php';


function loginUser($username, $password) {
    global $connect;

    $username = str_replace(' ', '', $username);
    $password = str_replace(' ', '', $password);

    $query = "SELECT id FROM users WHERE username='$username' AND password = '$password'";
    $result = mysqli_query($connect, $query);

    if (mysqli_num_rows($result) === 1) {
        $row = mysqli_fetch_assoc($result);
        $userid = $row['id'];

        session_start();
        $_SESSION['userid'] = $userid;

        header("Location: upload.php");
        exit;
    } else {
        return 'Invalid login credentials. Please try again.';
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $errorMsg = loginUser($_POST['username'], $_POST['password']);
}

mysqli_close($connect);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

    <style>
        body {
            background-color: #9cbfdd;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh; 
        }
        .container {
            max-width: 400px;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-control {
            border-radius: 3px;
        }
        .btn-primary {
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="container">
    <h1 class="text-center">Login</h1>
      <form action="" method="post">
          <div class="form-group">
              <input type="text" name="username" class="form-control" placeholder="Username" required>
          </div>
          <div class="form-group">
              <input type="password" name="password" class="form-control" placeholder="Password" required>
          </div>
          <button type="submit" class="btn btn-primary">Login</button>
          <?php if (!empty($errorMsg)): ?>
              <div class="alert alert-danger mt-3">
                  <?php echo $errorMsg; ?>
              </div>
          <?php endif; ?>
      </form>
    </div>
</body>
</html>
