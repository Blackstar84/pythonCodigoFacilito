function checkPalindrome(string) {

    // convert string to an array
    const convertirArreglo = string.split('');

    // reverse the array values
    const darVuelta = convertirArreglo.reverse();

    // convert array to string
    const convertirString = darVuelta.join('');

    if(string === convertirString) {
        console.log('It is a palindrome');
    }
    else {
        console.log('It is not a palindrome');
    }
}

//take input


checkPalindrome('ana')

