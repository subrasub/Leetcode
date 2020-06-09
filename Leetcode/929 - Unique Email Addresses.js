// https://leetcode.com/problems/unique-email-addresses/
// Tags - String

/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    
    var res = []
    
    for(var i = 0; i<emails.length; i++){
        //Get the index of the @ symbol
        var atme = emails[i].indexOf('@')
        
        //Get the local string
        var local = emails[i].slice(0, atme)
        
        //Remove the . from the local part 
        local = local.replace(/[.]/g, '')
        
        //If the local part has a +, then only count whatever is before that
        if(local.includes('+'))
            local = local.slice(0, local.indexOf('+'))
        
        //Domain after @
        var domain = emails[i].slice(atme)
        
        //Concatenate the strings
        var final = local.concat(domain)
        
        // If it doesn't exist, push into res
        if(!res.includes(final))
            res.push(final)
    }
    return res.length
};