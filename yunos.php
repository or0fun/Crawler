<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
		<style type="text/css">
			body{
				text-align:center;
			}
			.s_btn {
				width: 250px;
				height: 34px;
				border: 0;
				color: white;
				letter-spacing: 1px;
				background: #3385ff;
				border-bottom: 1px solid #2d78f4;
				outline: medium;
				-webkit-appearance: none;
				-webkit-border-radius: 0;
				font-size: 14px;
				cursor: pointer;
			}
			.s_ipt {
			    width: 526px;
			    height: 22px;
			    font: 16px/22px arial;
			    margin: 6px 0 0 7px;
			    padding: 0;
			    background: transparent;
			    border: 0;
			    outline: 0;
			    -webkit-appearance: none;
			}
			.fm {
			    clear: none;
			    margin: 11px 0 0 10px;
			}
			.s_ipt_wr {
			    border: 1px solid #b6b6b6;
			    border-color: #7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;
			    background: #fff;
			    display: inline-block;
			    vertical-align: top;
			    width: 539px;
			    height: 32px;
			    margin-right: 0;
			    border-right-width: 0;
			    border-color: #b8b8b8 transparent #ccc #b8b8b8;
			}
		</style>

		<script type="text/javascript">
			$(document).ready(function(){
				$("#crawler").click(function(){
					$("#crawler").html("正在爬...一会儿来刷新");
					htmlobj=$.ajax({url:"crawler.php?words=" + $("#words").val(),async:true});
				});
			});
		</script>
	</head>
	<body>

	
		<br/>
		<br/>
		<br/>

		<span class="s_ipt_wr">
			<input name="word" id="words" class="s_ipt" value="YunOS" maxlength="100" autocomplete="off">
		</span>
		<span class="s_btn_wr">
			<button id="crawler" class="s_btn">爬一下</button>
		</span>
		
	
		<br/>
		<br/>
		<br/>
		<?php
		$current_dir = 'Crawler';
		$dir = opendir($current_dir);
		echo "历史记录:";
		echo "<ul>";
		while(false !== ($file=readdir($dir))){
			if($file != "." && $file != ".." && strstr($file, ".xls")){
				echo "<li><a href='http://ie8384.com/pudding/Crawler/$file'>$file</a></li>";
			}
		}
		echo "</ul>";
		closedir($dir);
		?>
	</body>
</html>