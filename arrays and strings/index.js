//constructNote

//write a function, given an array of words available to use from a magazine, and words 
//contained in a note returns true if it is possible to recreate note using the words in the magazines 
//otherwise return false 


//first build hashmap => buildCharMap and use as a helper function
function buildCharMap(arr) { 
    let charMap = {}
    
    for( let char of arr){
        charMap[char] = ++charMap[char] || 1;
    }
    return charMap
}


function constructNote(magazine, note) { 
    //using the helper function buildCharMap we are going to build a character Map of the words in magazine
    //this helps to know the number of occurrences of the words in magazine
    let magazineMap = buildCharMap(magazine)

    //using the helper function buildCharMap we are going to build a character Map o the words in notes 
    //this helps to know the number of occurrences of the words in note
    let noteMap = buildCharMap(note)

    //loop through noteMap
    for (let key in noteMap){ 
        //compare occurrrences of each note word with occurrences of its version in magazine
        //if occurrences of word in not is more than taht in magazine
        if(noteMap[key] > magazineMap[key]){ 
            //return false
            return false
        }
        //if there is no occurrence of word in noe in that of magazine
        if(!magazineMap[key]){ 
            return false
        }
        return true
    }
}

const urlify = (str) => {
    let extended_str = '';
    let split_str = str.split(" ")
    for (let word of split_str){ 
        word += '%20';
        extended_str +=word
    }
    return extended_str
}