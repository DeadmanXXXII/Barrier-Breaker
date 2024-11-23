# Barrier-Breaker
Language barrier breaker.

The Helsinki-NLP/MarianMT models, developed by the Helsinki University team, support translations for over 1,000 language pairs. 

These models are pre-trained using the OPUS corpus, an open-source collection of multilingual parallel datasets. 

Below is a breakdown of the most commonly supported languages and ISO 639-1 codes:


---

Commonly Supported Languages

Here’s a list of languages supported by Helsinki-NLP/MarianMT, based on the available language pairs. Each entry includes the language name and its ISO 639-1 code:

Supported Languages:

1. Afrikaans (af)


2. Albanian (sq)


3. Amharic (am)


4. Arabic (ar)


5. Armenian (hy)


6. Azerbaijani (az)


7. Basque (eu)


8. Belarusian (be)


9. Bengali (bn)


10. Bosnian (bs)


11. Bulgarian (bg)


12. Catalan (ca)


13. Chinese (Simplified) (zh)


14. Croatian (hr)


15. Czech (cs)


16. Danish (da)


17. Dutch (nl)


18. English (en)


19. Estonian (et)


20. Finnish (fi)


21. French (fr)


22. Galician (gl)


23. Georgian (ka)


24. German (de)


25. Greek (el)


26. Gujarati (gu)


27. Hebrew (he)


28. Hindi (hi)


29. Hungarian (hu)


30. Icelandic (is)


31. Indonesian (id)


32. Irish (ga)


33. Italian (it)


34. Japanese (ja)


35. Kannada (kn)


36. Kazakh (kk)


37. Korean (ko)


38. Kurdish (Kurmanji) (ku)


39. Kyrgyz (ky)


40. Latvian (lv)


41. Lithuanian (lt)


42. Macedonian (mk)


43. Malay (ms)


44. Malayalam (ml)


45. Maltese (mt)


46. Marathi (mr)


47. Mongolian (mn)


48. Nepali (ne)


49. Norwegian (no)


50. Pashto (ps)


51. Persian (Farsi) (fa)


52. Polish (pl)


53. Portuguese (pt)


54. Punjabi (pa)


55. Romanian (ro)


56. Russian (ru)


57. Serbian (sr)


58. Sinhala (si)


59. Slovak (sk)


60. Slovenian (sl)


61. Somali (so)


62. Spanish (es)


63. Swahili (sw)


64. Swedish (sv)


65. Tamil (ta)


66. Telugu (te)


67. Thai (th)


68. Turkish (tr)


69. Ukrainian (uk)


70. Urdu (ur)


71. Uzbek (uz)


72. Vietnamese (vi)


73. Welsh (cy)


74. Zulu (zu)




---


translation_tool/

│

├── app.py 

 Main Flask application
 
├── requirements.txt     

 Python dependencies
 
├── static/                      

 Static files (CSS, JS, images)
 
├── templates/       

 HTML templates for the UI
 
│   └── index.html       

Upload and translate interface

├── uploads/        

 Directory for uploaded files
 
├── outputs/         


 Directory for translated files
├── modules/      

 Custom modules
 
│   ├── file_handler.py    

 Handles file reading/writing
 
│   ├── translator.py


 Language translation logic
 
│   └── grammar_corrector.py  

 Grammar and punctuation correction
 
├── README.md          
 
 Documentation
 
└── .gitignore       

 Git ignore file


 


