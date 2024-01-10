<?php
$station = $_POST['station'];

//$command = "sudo python3 piRC_manual.cpython-34.pyc $status 2>&1";y
$command = "./nws.py $station 2>&1";
$output = shell_exec($command);
//exec($command, $output);

print "
<html>
<title> NWC Latest</title>
<body>";

include('buttons.html');

print "
<text_area><pre>Result: $output</pre></text_area>
<script>
console.log('PHP-input:" .$station. "');
</script>
</body>
</html>
";
?>
