<?php
$requestedDir = $_SERVER['REQUEST_URI'];

if (preg_match('/^\/archives\/[a-f0-9\-]+$/', $requestedDir) && is_dir($_SERVER['DOCUMENT_ROOT'] . $requestedDir)) {
    return false;
} else {
    http_response_code(403);
    echo "Access forbidden";
}
?>