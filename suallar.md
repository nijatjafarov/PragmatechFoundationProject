1. Translator ve assebler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
    - Translator əsasən yüksək səviyəli dildə yazılmış source code-u aşağı səviyə olan machine code-a çevirən bir alətdir. Bu baxımdan Compiler, interpreter və Assembler kimi çeviricilərə ümumi olaraq Translator deyilir. Assembler isə aşağı səviyyə Assembly dilində yazılmış kodu maşın dilinə çevirən çeviricidir.
2. Rəqəm və ədədlərin maşın dilinə tərcümə olunma prosesini bilirik. Bəs hərflər və simvollar necə tərcümə olunur?
    - Hərflər və simvollar maşın dilinə bəlirlənmiş standartlar əsasında çevrilirlər. Bu standartlara verilə biləcək örnəklər ASCİİ və Unicode-dur. ASCİİ(American Standard Code for Information Interchange) açılışı "İnformasiya mübadiləsi üçün amerikan standart kodu"-dur. Əsasında ingilis əlifbası üçün yazılmış standartdır və 256 simvolu əhatə edir. Lakin, dünyada fərqli dillər və simvollar olduğu üçün ASCİİ qlobal informasiya mübadiləsi üçün kifayət etmir və nəticədə Unicode yaradılıb. Unicode-da simvollar üçün 1 112 064 yer ayrılıb və indiyə qədər bu yerlərin 100 000-dən çoxu istifadə olunub.
3. Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri hansılardır və qısaca izahatlarını yazın
    - Əksər proqramlaşdırma dillərində istifadə olunan təməl data növlərinə aşağıdakıları nümuna göstərmək olar:
        - Integer
        - Floating-point number
        - Character
        - String
        - Boolean

        **Integer**: proqramlaşdırma zamanı tam ədədlərin yazılması məqsədi ilə istifadə olunur və bu baxımdan fundamental data növü hesab edilə bilər.
        **Floating-point number**: həqiqi ədədlərin istifadə olunması üçün lazımdır.
        **Character**: hərf, rəqəm, simvolların ASCİİ və ya Unicode-da olan encoding qarşılığından istifadə etmək məqsədilə işlədilir.
        **String**: mətn formasında olan datalardan istifadə üçün mövcuddur.
        **Boolean**: mümkün iki qiymətdən birini alan data tipi. Doğru və ya yalnış kimi məntiqi nəticələr əldə etmək üçün istifadə olunur.
