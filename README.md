Change permissions of file to make it executable: <br />
```chmod +x doomscramble.py``` <br />
Use python 3 to run file: <br />
```python ./doomscramble.py``` <br />

Background information gathered by using the [wayback machine](https://web.archive.org/web/20221114212355/http://justsolve.archiveteam.org/wiki/Doom_cheat_code_encryption) in [this PDF](doom_cheat_code_encryption.pdf)

### Doom cheat code encryption
Doom cheat code encryption was used in the original 1993 version of Doom to make the cheat codes a little harder for hackers to find, so they didn't appear in the raw binary code as plain ASCII characters. (Of course, the hackers found them anyway.) Twitter user @Foone described it in a 2019 thread.

This low-grade encryption is done by shifting the bits of 8-bit numbers (which can represent single ASCII characters) which reverses the order of the bits except for those representing 4 and 32. The shifted values are stored in a lookup table in the Doom program.

### Details
As described by @Foone, who has allowed these descriptions to be released as CC0 so they can be used here:

So Doom (1993) has a neat bit of encryption in it. It's not very strong encryption, but it's still encryption. 
And it's not used in any sort of way you'd normally expect: not copy protection, or multiplayer anti-cheat, or anti-tampering on saves... It's to slow down FAQs. 

So here's the code I'm talking about, the macro SCRAMBLE 
It looks annoyingly complicated but it's not, really. 
It's taking an 8-bit number and shifting around some of the bits. 

![image](https://github.com/user-attachments/assets/a870a215-64c8-41e3-aa60-3610d00e4d72)


If you diagram out what's happening, it makes slightly (BUT ONLY SLIGHTLY) more sense. 
It kinda looks like they started with a a "reverse the order of these bits" function but then switched it so the 4 and 32 don't get switched, they just go straight through. 

![image](https://github.com/user-attachments/assets/6307fc4a-6e94-4080-81e1-884e3cb89a63)


So, how is this code used? 
Well, in m_cheat.c, it's used to build a lookup table which has all the values pre-encrypted, so it can quickly look them up later. Then, when you press a key, it translates it through this table: 

![image](https://github.com/user-attachments/assets/b2d350d3-8fba-4a63-ac66-7a4cba7a6947)


The thread goes on with more discussion of how these codes were used and discovered. It's worthwhile reading for people into this sort of trivia.
