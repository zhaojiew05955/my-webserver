<html>
    <head>
    <title>my infomatiom!</title>
    </head>
    <body>
    <h1>My infomation</h1>
    <p>name:
    %if name:
        Hi <b>{{ name }}</b>
    %else:
        <i>Hello world</i>
    %end
    </p>
    <p>age:{{ age.get('age') }}</p>
    <p>weight:{{ weight.get('weight')}}</p>
    <p>blog:{{ blog }}</p>
    <p>friends:
    %for i in SNS:
        {{ i }} 
    %end
    </p>
    </body>
</html>