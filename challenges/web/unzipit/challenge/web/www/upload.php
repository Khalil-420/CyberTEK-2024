<?php
error_reporting(E_ALL & ~E_DEPRECATED);
ini_set('display_errors', 0);
session_start();



if (!isset($_SESSION['userid'])) {
    header("Location: index.php"); 
    exit;
}

$success = false;
$badZip = false;

function gen_uuid() {
    return sprintf( '%04x%04x-%04x-%04x-%04x-%04x%04x%04x',
        mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ),
        mt_rand( 0, 0xffff ),
        mt_rand( 0, 0x0fff ) | 0x4000,
        mt_rand( 0, 0x3fff ) | 0x8000,
        mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff )
    );
}

function zipIsValid($path) {
  $zip = zip_open($path);
  if (is_resource($zip)) {
    zip_close($zip);
    return true;
  } else {
    return false;
  }
}


if(isset($_FILES['archive'])) {
  $dest = 'archives/'.gen_uuid();
  $zipFile = $_FILES['archive']['tmp_name'];
  mkdir($dest);
  if (zipIsValid($zipFile)) {
    exec("unzip $zipFile -d $dest");
    if (file_exists("$dest/.htaccess")) {
      unlink("$dest/.htaccess");
    }
    $success = true;
  }
  else {
    $badZip = true;
  }
}
require_once 'header.php';
?>
<div class="row">
  <div class="page-header">
    <h3>Archive Extractor</h3>
  </div>
  <p>Received a zip file and unsure how to unzip it? No worries! We've got you covered.</p>
  <?php if ($success): ?>
    <div class="alert alert-success">
      <strong>Woo hoo!</strong> We've unzipped your files. You can view them <a href="<?php echo $dest;?>">here</a>
    </div>
  <?php endif; ?>
  <?php if ($badZip): ?>
    <div class="alert alert-danger">
      <strong>Error</strong> Bad zip file</a>
    </div>
  <?php endif; ?>
  <form action="" method="post" enctype="multipart/form-data" />
    <input type="file" name="archive" />
    <br />
    <input type="submit" value="Unzip!" class="btn btn-primary" />

    <a href="logout.php" class="nav-item nav-link px-3"><i class="fas fa-sign-out-alt"><span class="nav-text">&nbsp; Logout</span></i></a>
  </form>
</div>
<?php
require_once 'footer.php';

?>
