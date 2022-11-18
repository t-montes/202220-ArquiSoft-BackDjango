console.log("DJango Javascript is working 1");

var firstTime = localStorage.getItem('firstTime');

if (firstTime == null) {
    localStorage.setItem('firstTime', 'true');
    console.log("First time");
} else {
    if (firstTime == 'true') {
        localStorage.setItem('firstTime', 'false');
    } else {
        localStorage.setItem('firstTime', 'true');
    }
    console.log("Not first time; changed");
}

console.log("DJango Javascript is working 2");

localStorage.setItem('user', user)

console.log("DJango Javascript is working 3");

console.log("user ", user);

