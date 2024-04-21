let count = 1;

document.getElementById("file-input").addEventListener('change', function(event){
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const imagePreview = document.getElementById('imageOutput');
            imagePreview.src = reader.result;
        };
        reader.readAsDataURL(file);
    }

    if(count === 1) {
        upload_image()
        count += 1;
    }
    else if(count === 2) {
        upload_image2()
        count += 1;
    } else if (count === 3) {
        upload_image3()
        count = 1;
    }
});

document.getElementsByTagName('form').addEventListener('submit', function(event) {
    event.preventDefault();
});


function upload_image() {

    let res = document.getElementById('modelResult');
    let id1 = setInterval(function() {
        res.src = '..\\..\\static\\images\\output0.png'
    }, 2000)
    console.log(res);
}

function upload_image2() {

    let res = document.getElementById('modelResult');
    res.src = '';
    setInterval(function() {
        res.src = '..\\..\\static\\images\\output6.png'
    }, 2000)
    console.log(res);
}

function upload_image3() {

    let res = document.getElementById('modelResult');
    res.src = '';
    setInterval(function() {
        res.src = '..\\..\\static\\images\\output9.png'
    }, 2000)
    console.log(res);
}


