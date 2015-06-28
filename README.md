# Glottal Categorizer tsv

**Glottal Categorizer tsv is a Python script which reads a tsv file of glottal-stop-containing Nishnaabe words (Pic River dialect), Nishnaabe parts of speech, and English glosses. The script then returns a categorization of all the file's Nishnaabe entries into the particular glottal stop grapheme regex pattern(s) to which each word belongs. Each returned "glottal stop grapheme regex pattern" contains at least one occurrence of a Nishnaabe word (from within the tsv file of Nishnaabe words) containing the following sequence:**

**Left-hand-side grapheme -> Glottal stop -> Right-hand-side grapheme.**

## Sample Output

```
------([^a]|^)ahm------
dbahminaan	nm	your choice of English gloss

------([^a]|^)ahn([^d|g|ǧ|h|ȟ|j|s|y|z|zh|zȟ]|$)------
ǧpahnaad	vta	your choice of English gloss

------([^a]|^)ahw------
zgahwaad	vta	your choice of English gloss
bgwahwaad	vta	your choice of English gloss

------aaha([^a]|$)------
webaahang	vii	your choice of English gloss

------aahaa------
waakaahaaǩnigan	ni	your choice of English gloss
baataahaad	vta	your choice of English gloss

------aahg------
wshkiwaakaahganed	vai	your choice of English gloss

------aaȟg------
waanaaȟgong	vii	your choice of English gloss

------bha([^a]|$)------
aabhamwaad	vta	your choice of English gloss
gwaabwebhang	vti	your choice of English gloss


. . .


------who([^o]|$)------
wzaawhod	vai	your choice of English gloss

------([^n]|^)yhaa------
wshkayhaawid	vai	your choice of English gloss

------([^n]|^)yhii------
zaagjiyhiing	av	your choice of English gloss
shpayhii	av	your choice of English gloss
nikeyhiing	av	your choice of English gloss

------([^n]|^)zhhw------
bbaamnizhhwaad	vta	your choice of English gloss

The number of hypothetically possible glottal pattern categories is: 3948

The number of observed glottal pattern categories is: 58

The observed glottal pattern categories are, as regexen, 
["'ha([^a]|$)", "'hi([^i]|$)", '([^a]|^)aha([^a]|$)', '([^a]|^)ahaa',
'([^a]|^)ahg', '([^a]|^)ahm', '([^a]|^)ahn([^d|g|ǧ|h|ȟ|j|s|y|z|zh|zȟ]|$)',
'([^a]|^)ahw', 'aaha([^a]|$)', 'aahaa', 'aahg', 'aaȟg', 'bha([^a]|$)', 'bhaa',
'bhi([^i]|$)', 'bhoo', '([^n]|^)dha([^a]|$)', '([^n]|^)dhi([^i]|$)',
'([^n]|^)dhoo', '([^n]|^)dhw', 'ehaa', 'ehg', 'ehm', 'eho([^o]|$)',
'eȟs([^h|ȟ|k|ǩ]|$)', 'ehshk', '([^n]|^)ghi([^i]|$)', '([^n]|^)ghw',
'([^n]|^)ǧhi([^i]|$)', '([^n]|^)ǧhw', '([^i]|^)ihaa', '([^i]|^)iho([^o]|$)',
'iiha([^a]|$)', 'iihd', 'iihg', 'iiho([^o]|$)', 'iihw', '([^n]|^)jhaa',
'([^n]|^)jhi([^i]|$)', '([^s|sh]|^)kha([^a]|$)', '([^s|sh]|^)khaa',
'([^s|sh]|^)ǩha([^a]|$)', '([^s|sh]|^)ǩhi([^i]|$)', '([^s|sh]|^)ǩho([^o]|$)',
'([^s|sh]|^)ǩhw', 'mhe', 'mhi([^i]|$)', 'mhii', '([^o]|^)ohaa', 'oohg', 'oohw',
'phaa', 'shkhi([^i]|$)', 'whaa', 'who([^o]|$)', '([^n]|^)yhaa', '([^n]|^)yhii',
'([^n]|^)zhhw']
```



## Current project member:

John Paul Montano
[http://jpmontano.com](http://jpmontano.com)
