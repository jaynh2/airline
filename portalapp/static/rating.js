// document.querySelectorAll('.rating input').forEach(radio => {
//     radio.addEventListener('change', () => {
//         const rating = parseInt(radio.value);
//         // alert("rating is " + rating)
//         if(rating == 5)
//         {
//             document.getElementById('improve-message').style.display = 'none';
//             document.getElementById('thank-you-message').style.display = 'none';
//             document.getElementById('delighted').style.display = 'block';
//         }
//         elif (rating < 3) 
//         {
//             document.getElementById('thank-you-message').style.display = 'none';
//             document.getElementById('improve-message').style.display = 'block';
//             document.getElementById('delighted').style.display = 'none';
//         } 
//         else 
//         {
//             document.getElementById('improve-message').style.display = 'none';
//             document.getElementById('thank-you-message').style.display = 'block';
//             document.getElementById('delighted').style.display = 'none';
//         }
//     });
// });



document.querySelectorAll('.rating input').forEach(radio => {
    radio.addEventListener('change', () => {
        const rating = parseInt(radio.value);
        // alert("rating is " + rating)
        if (rating == 5) 
        {
            document.getElementById('improve-message').style.display = 'none';
            document.getElementById('thank-you-message').style.display = 'none';
            document.getElementById('delighted').style.display = 'block';
        } 
        else if (rating < 3) 
        {
            document.getElementById('thank-you-message').style.display = 'none';
            document.getElementById('improve-message').style.display = 'block';
            document.getElementById('delighted').style.display = 'none';
        } 
        else 
        {
            document.getElementById('improve-message').style.display = 'none';
            document.getElementById('thank-you-message').style.display = 'block';
            document.getElementById('delighted').style.display = 'none';
        }
    });
});