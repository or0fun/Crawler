<?php
	ignore_user_abort();//关掉浏览器，PHP脚本也可以继续执行.
	set_time_limit(0);// 通过set_time_limit(0)可以让程序无限制的执行下去
	$words = str_replace(" ","+",$_GET['words']);
	echo "python Crawler/yun.py ".$words . " " . $_GET['fromdate'];
	$cmd = exec("python Crawler/yun.py ".$words . " " . $_GET['fromdate']);
	echo $cmd;
	echo "running google news";
?>