<?
include_once("phpolait/phpolait.php");

class EchoService {
    function myecho($msg) { return $msg; }

    function myreverse($msg) { return strrev($msg); }

    function myuppercase($msg) { return strtoupper($msg); }

    function mylowercase($msg) { return strtolower($msg); }
}

$server = new JSONRpcServer(new EchoService(), array("echo"=>"myecho", "reverse"=>"myreverse", "uppercase"=>"myuppercase", "lowercase"=>"mylowercase"));
?>
