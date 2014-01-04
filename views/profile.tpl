<head>
    <style>
        .title{
            border-bottom:3px solid;
        }
    </style>
</head>
<body>
    <img src="http://www.w3school.com.cn/i/eg_tulip.jpg"  alt="上海鲜花港 - 郁金香" />
    <div class=title>introduction</div>
    <text>write your profile</text>
    <div class=title>expectation</div>
    <label>describe your lover</label>
        %if name == 'World':
            <h1>Hello {{name}}!</h1>
            <p>This is a test.</p>
        %else:
            <h1>Hello {{name.title()}}!</h1>
            <p>How are you?</p>
        %end
</body>
