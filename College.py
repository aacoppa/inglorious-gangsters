from User import User
from bs4 import BeautifulSoup
import urllib2
import math

location_weight = 1.3
sat_below_range_weight = 2
sat_above_range_weight = 1.3
sat_weight = 1.3
gpa_below_weight = 2
gpa_above_weight = 1.3
rank_weight = .1
class College:
    
    def __init__(self, name, location, rank, sats, size, tuition, address):
        self.name = name
        self.location = location 
        self.rank = rank
        self.sats = sats
        self.tuition = tuition
        self.size = size
        self.address = address
    def get_difficulty_comparison(self, user_level):
        """
            returns value of comparison between user and school
        """
        compare_value = 0
        
        college_level = self.get_difficulty()
        
        total_value = user_level + college_level
        return total_value
        
    def find_location(self):
        key = "AIzaSyAKd5dbb90Go0U3YNo4veBil91D0u2DBio"
        url = "https://maps.googleapis.com/maps/api/place/autocomplete/xml?input={0}&sensor=false&key={1}".format(self.name.replace(" ", "&"), key)
        result = urllib2.urlopen(url).read()
        print result
        exit()
    def get_difficulty(self):
        """
            returns the difficulty of getting into the school for for a user
        """
        difficulty = 0.0
        difficulty -= (300 - self.rank) / 300.0
        if not self.sats:
            return difficulty
        for subject in self.sats:
            difficulty += self.sat_range_conversion(subject)
        return difficulty
    def sat_range_conversion(self, subject):
        """
            Converts SAT score to weighted difficulty value
        """
        if not self.sats or not subject in self.sats:
            return .5
        return (self.sats[subject].bottom + self.sats[subject].top) / 1600 * sat_weight
    def print_college(self):
        if not self.sats:
            print "%s, no SAT data available" % (self.name)
            return
        print "{0} Math {1}-{2} Reading {3}-{4}".format(self.name, self.sats['math'].bottom,
              self.sats['math'].top, self.sats['reading'].bottom, self.sats['reading'].top)

    #def gpa_conversion(value):
    #    if value >= self.gpa
colleges = [
"Princeton University",
"Harvard University",
"Yale University",
"Columbia University",
"Stanford University",
"University of Chicago",
"Duke University",
"Massachusetts Institute of Technology",
"University of Pennsylvania",
"California Institute of Technology",
"Dartmouth College",
"Johns Hopkins University",
"Northwestern University",
"Brown University",
"Washington University in St. Louis",
"Cornell University",
"Vanderbilt University",
"Rice University",
"University of Notre Dame",
"Emory University",
"Georgetown University",
"University of California--Berkeley",
"Carnegie Mellon University",
"University of California--Los Angeles",
"University of Southern California",
"University of Virginia",
"Wake Forest University",
"Tufts University",
"University of Michigan--Ann Arbor",
"University of North Carolina--Chapel Hill",
"Boston College",
"Brandeis University",
"College of William and Mary",
"Georgia Institute of Technology",
"Case Western Reserve University",
"Pennsylvania State University--University Park",
"University of California--Davis",
"University of California--San Diego",
"Boston University",
"Lehigh University",
"Rensselaer Polytechnic Institute",
"University of California--Santa Barbara",
"University of Illinois--Urbana-Champaign",
"University of Wisconsin--Madison",
"University of Miami",
"Yeshiva University",
"Northeastern University",
"University of California--Irvine",
"University of Florida",
"George Washington University",
"Ohio State University--Columbus",
"Tulane University",
"University of Texas--Austin",
"University of Washington",
"Fordham University",
"Pepperdine University",
"University of Connecticut",
"Southern Methodist University",
"University of Georgia",
"Brigham Young University--Provo",
"Clemson University",
"Syracuse University",
"University of Maryland--College Park",
"University of Pittsburgh",
"Worcester Polytechnic Institute",
"Purdue University--West Lafayette",
"Rutgers, the State University of New Jersey--New Brunswick",
"Texas A&M University--College Station",
"University of Minnesota--Twin Cities",
"Virginia Tech",
"Michigan State University",
"University of Iowa",
"American University",
"Baylor University",
"Clark University",
"Indiana University--Bloomington",
"Stevens Institute of Technology",
"Stony Brook University--SUNY",
"Texas Christian University",
"University of Vermont",
"SUNY College of Environmental Science and Forestry",
"University of Alabama",
"University of California--Santa Cruz",
"University of Colorado--Boulder",
"University of Tulsa",
"Auburn University",
"Colorado School of Mines",
"Binghamton University--SUNY",
"Drexel University",
"University of Missouri",
"University of New Hampshire",
"Iowa State University",
"Loyola University Chicago",
"North Carolina State University--Raleigh",
"St. Louis University",
"University of Kansas",
"University of Nebraska--Lincoln",
"University of Oklahoma",
"Illinois Institute of Technology",
"University at Buffalo--SUNY",
"University of Oregon",
"University of California--Riverside",
"University of Dayton",
"University of South Carolina",
"University of St. Thomas",
"University of the Pacific",
"Michigan Technological University",
"University of San Francisco",
"University of Arizona",
"University of Kentucky",
"The Catholic University of America",
"Clarkson University",
"Colorado State University",
"DePaul University",
"Duquesne University",
"Temple University",
"University of Utah",
"Missouri University of Science & Technology",
"Polytechnic Institute of New York University",
"Hofstra University",
"Kansas State University",
"Louisiana State University--Baton Rouge",
"New School",
"Ohio University",
"University of Cincinnati",
"George Mason University",
"Arizona State University",
"Howard University",
"Mississippi State University",
"Oklahoma State University",
"New Jersey Institute of Technology",
"University of Mississippi",
"Adelphi University",
"Illinois State University",
"San Diego State University",
"St. John's University",
"University of Alabama--Birmingham",
"University of Rhode Island",
"University of Hawaii--Manoa",
"University of Maryland--Baltimore County",
"University of Massachusetts--Lowell",
"Maryville University of St. Louis",
"Texas Tech University",
"University of Idaho",
"University of La Verne",
"University of Louisville",
"University of Wyoming",
"Florida Institute of Technology",
"University of Maine",
"Virginia Commonwealth University",
"University of Central Florida",
"University of South Florida",
"Azusa Pacific University",
"Pace University",
"St. Mary's University of Minnesota",
"University of North Dakota",
"Biola University",
"Indiana University of Pennsylvania",
"Northern Illinois University",
"Southern Illinois University--Carbondale",
"Andrews University",
"Ball State University",
"Bowling Green State University",
"Central Michigan University",
"Edgewood College",
"Immaculata University",
"Louisiana Tech University",
"New Mexico State University",
"North Dakota State University",
"University of Colorado--Denver",
"University of Houston",
"University of North Carolina--Greensboro",
"University of South Dakota",
"Utah State University",
"Kent State University",
"Montana State University",
"South Dakota State University",
"University of Missouri--Kansas City",
"University of Montana",
"University of North Carolina--Charlotte",
"Ashland University",
"Barry University",
"Benedictine University",
"Bowie State University",
"Cardinal Stritch University",
"Clark Atlanta University",
"Cleveland State University",
"East Tennessee State University",
"Florida A&M University",
"Florida Atlantic University",
"Florida International University",
"Georgia Southern University",
"Georgia State University",
"Idaho State University",
"Indiana State University",
"Indiana University-Purdue University--Indianapolis",
"Jackson State University",
"Lamar University",
"Lynn University",
"Middle Tennessee State University",
"Morgan State University",
"National-Louis University",
"North Carolina A&T State University",
"Northern Arizona University",
"Nova Southeastern University",
"Oakland University",
"Old Dominion University",
"Our Lady of the Lake University",
"Portland State University",
"Regent University",
"Sam Houston State University",
"South Carolina State University",
"Spalding University",
"Tennessee State University",
"Texas A&M University--Commerce",
"Texas A&M University--Corpus Christi",
"Texas A&M University--Kingsville",
"Texas Southern University",
"Texas Woman's University",
"Trevecca Nazarene University",
"Trinity International University",
"University of Akron",
"University of Alaska--Fairbanks",
"University of Arkansas--Little Rock",
"University of Louisiana--Lafayette",
"University of Massachusetts--Boston",
"University of Memphis",
"University of Missouri--St. Louis",
"University of Nebraska--Omaha",
"University of Nevada--Las Vegas",
"University of New Orleans",
"University of Northern Colorado",
"University of North Texas",
"University of South Alabama",
"University of Southern Mississippi",
"University of Texas--Arlington",
"University of Texas--El Paso",
"University of Texas--San Antonio",
"University of Toledo",
"University of West Florida",
"University of Wisconsin--Milwaukee",
"Wayne State University",
"Wichita State University",
"Wright State University",
"Argosy University",
"California Institute of Integral Studies",
"Capella University",
"Colorado Technical University",
"Northcentral University",
"Trident University International",
"Union Institute and University",
"University of Phoenix",
"Walden University",
"Wilmington University",
]
colleges_with_sat = [
"Albion College",  480, 640, 460, 620,
"Alfred University",       500, 600, 480, 580,
"Allegheny College",       560, 650, 540, 650,
"American University",     570, 670, 590, 690,
"Amherst College", 670, 760, 670, 770,
"Arizona State University",        500, 630, 480, 610,
"Auburn University",       550, 650, 530, 630,
"Austin College",  570, 670, 560, 660,
"Babson College",  610, 700, 550, 640,
"Bard College",    600, 670, 650, 710,
"Barnard College", 620, 710, 630, 730,
"Bates College",   630, 720, 630, 710,
"Baylor University",       570, 670, 550, 660,
"Bellarmine University",   490, 600, 500, 600,
"Beloit College",  560, 690, 550, 710,
"Bennington College",      560, 660, 620, 720,
"Bentley University",      590, 670, 530, 620,
"Berea College",   530, 630, 540, 660,
"Birmingham-Southern College",     510, 610, 500, 610,
"Boston College",  640, 740, 620, 710,
"Boston University",       610, 720, 570, 670,
"Bowdoin College", 670, 760, 670, 760,
"Brandeis University",     620, 740, 610, 710,
"Brigham Young University",        590, 690, 580, 690,
"Brown University",        660, 770, 660, 760,
"Bryant University",       540, 640, 510, 600,
"Bryn Mawr College",       590, 720, 600, 710,
"Bucknell University",     620, 710, 580, 680,
"California Institute of Technology",      770, 800, 720, 780,
"California Polytechnic State University", 580, 680, 540, 650,
"Calvin College",  540, 690, 520, 670,
"Carleton College",        670, 760, 670, 760,
"Carnegie Mellon University",      690, 790, 630, 730,
"Case Western Reserve University", 660, 760, 600, 700,
"Catawba College", 450, 550, 430, 540,
"Centenary College of Louisiana",  430, 780, 490, 620,
"Centre College",  580, 700, 560, 690,
"Chapman University",      560, 660, 550, 650,
"Claremont McKenna College",       660, 760, 650, 760,
"Clark University",        530, 640, 530, 640,
"Clarkson University",     560, 660, 500, 610,
"Clemson University",      590, 680, 560, 660,
"Coe College",     500, 650, 490, 610,
"Colby College",   630, 720, 610, 710,
"Colgate University",      640, 720, 630, 730,
"College of Charleston",   560, 650, 550, 650,
"College of the Atlantic", 540, 680, 610, 690,
"College of the Holy Cross",       620, 680, 600, 700,
"College of the Ozarks",   440, 560, 510, 610,
"College of William and Mary",     620, 720, 360, 740,
"Colorado College",        610, 710, 630, 720,
"Colorado School of Mines",        630, 720, 570, 670,
"Colorado State University",       520, 640, 500, 620,
"Columbia University",     700, 790, 690, 780,
"Connecticut College",     620, 700, 620, 710,
"Cooper Union",    610, 770, 620, 710,
"Cornell College", 540, 690, 530, 680,
"Cornell University",      670, 780, 640, 740,
"Creighton University",    540, 660, 530, 630,
"Dartmouth College",       680, 780, 670, 780,
"Davidson College",        640, 720, 630, 720,
"Denison University",      600, 680, 600, 720,
"DePaul University",       510, 630, 530, 640,
"DePauw University",       550, 680, 530, 650,
"Dickinson College",       600, 690, 590, 690,
"Drew University", 480, 600, 490, 620,
"Drexel University",       580, 680, 540, 640,
"Duke University", 690, 790, 670, 760,
"Duquesne University",     530, 610, 510, 590,
"Earlham College", 530, 660, 550, 700,
"Eckerd College",  500, 610, 510, 620,
"Elon University", 560, 660, 570, 660,
"Emerson College", 560, 650, 590, 680,
"Emory University",        660, 760, 620, 710,
"Fairfield University",    550, 630, 530, 620,
"Fisk University", 400, 570, 410, 540,
"Flagler College", 520, 580, 540, 600,
"Florida State University",        560, 640, 560, 640,
"Fordham University",      590, 680, 570, 670,
"Franklin & Marshall College",     610, 710, 600, 690,
"Olin College of Engineering",     730, 790, 700, 780,
"Furman University",       560, 660, 550, 650,
"George Mason University", 530, 630, 520, 620,
"Georgetown University",   660, 750, 650, 750,
"Georgia Institute of Technology", 660, 760, 600, 700,
"Gettysburg College",      610, 670, 600, 690,
"Gonzaga University",      550, 650, 540, 640,
"Goucher College", 480, 620, 510, 640,
"Grinnell College",        650, 750, 630, 750,
"Grove City College",      550, 680, 550, 680,
"Guilford College",        490, 660, 480, 620,
"Gustavus Adolphus College",       530, 660, 550, 680,
"Hamilton College",        650, 740, 650, 740,
"Hampden-Sydney College",  510, 610, 490, 620,
"Hampshire College",       540, 650, 600, 700,
"Hampton University",      478, 593, 480, 594,
"Hanover College", 490, 600, 500, 620,
"Harvard College", 710, 790, 700, 800,
"Harvey Mudd College",     740, 800, 680, 770,
"Haverford College",       660, 760, 650, 760,
"Hendrix College", 540, 670, 550, 680,
"Hillsdale College",       570, 690, 630, 740,
"Hiram College",   440, 570, 440, 560,
"Hobart and William Smith Colleges",       570, 660, 570, 650,
"Hofstra University",      540, 630, 530, 630,
"Hollins University",      460, 590, 500, 650,
"Howard University",       480, 580, 490, 580,
"Illinois Institute of Technology",        610, 710, 510, 630,
"Illinois Wesleyan University",    570, 700, 540, 650,
"Indiana University- Bloomington", 510, 620, 540, 600,
"Indiana University of Pennsylvania",      450, 540, 440, 530,
"Iowa State University",   530, 680, 460, 620,
"James Madison University",        530, 630, 520, 620,
"Johns Hopkins University",        670, 770, 640, 740,
"Juniata College", 540, 650, 530, 650,
"Kalamazoo College",       530, 650, 540, 670,
"Kenyon College",  610, 680, 630, 730,
"Knox College",    580, 690, 570, 720,
"Lafayette College",       610, 710, 580, 680,
"Lake Forest College",     530, 670, 530, 620,
"Lawrence University",     580, 710, 580, 720,
"Lehigh University",       630, 730, 570, 670,
"Lewis & Clark College",   590, 670, 600, 700,
"Louisiana State University",      520, 630, 500, 620,
"Loyola College in Maryland",      540, 630, 540, 630,
"Loyola Marymount University",     560, 660, 550, 640,
"Loyola University New Orleans",   510, 620, 530, 650,
"Loyola University of Chicago",    540, 650, 550, 650,
"Lynchburg College",       450, 550, 450, 550,
"Macalester College",      640, 730, 630, 740,
"Manhattanville College",  450, 560, 450, 560,
"Marist College",  550, 640, 530, 620,
"Marlboro College",        520, 650, 560, 730,
"Marquette University",    550, 650, 520, 630,
"Massachusetts Institute of Technology",   740, 800, 670, 770,
"McGill University",       630, 730, 630, 730,
"Mercer University",       540, 640, 530, 630,
"Miami University",        550, 660, 530, 630,
"Michigan State University",       540, 680, 430, 590,
"Michigan Technological University",       520, 650, 580, 680,
"Middlebury College",      640, 740, 630, 740,
"Mills College",   510, 620, 540, 660,
"Millsaps College",        520, 620, 498, 630,
"Monmouth University",     490, 580, 470, 560,
"Moravian College",        470, 550, 480, 590,
"Mount Holyoke College",   610, 700, 610, 720,
"Muhlenberg College",      560, 680, 560, 680,
"New College of Florida",  570, 670, 620, 740,
"New York University",     630, 740, 620, 710,
"North Carolina State University", 580, 670, 550, 630,
"Northeastern University", 650, 740, 630, 720,
"Northwestern University", 700, 780, 680, 760,
"Oberlin College", 620, 720, 650, 740,
"Oglethorpe University",   510, 610, 530, 620,
"Ohio Northern University",        540, 660, 510, 620,
"Ohio State University",   610, 710, 540, 650,
"Ohio University", 490, 610, 480, 590,
"Ohio Wesleyan University",        520, 640, 510, 620,
"Penn State University",   560, 670, 530, 630,
"Pepperdine University",   570, 680, 550, 650,
"Pitzer College",  590, 680, 580, 710,
"Pomona College",  690, 780, 690, 790,
"Princeton University",    710, 800, 700, 790,
"Providence College",      520, 630, 530, 640,
"Purdue University",       550, 620, 510, 620,
"Quinnipiac University",   510, 610, 490, 580,
"Randolph-Macon College",  490, 590      , 490, 590,
"Randolph-Macon Woman's College",  490, 610      , 480, 610,
"Reed College",    620, 720      , 660, 750,
"Rensselaer Polytechnic Institute",        670, 770      , 620, 720,
"Rhodes College",  580, 680      , 590, 690,
"Rice University", 700, 780      , 660, 750,
"Rider University",        470, 570      , 460, 560,
"Ripon College",   510, 680      , 490, 630,
"Rochester Institute of Technology",       570, 680      , 540, 650,
"Rollins College", 540, 640      , 550, 640,
"Rose-Hulman Institute of Technology",     640, 750      , 540, 670,
"Rutgers University",      540, 670, 500, 620,
"Saint Anselm College",    520, 620      , 540, 610,
"Saint Louis University",  540, 670      , 530, 660,
"Saint Mary's College of California",      500, 610      , 500, 600,
"Saint Michael's College", 520, 620      , 530, 630,
"Saint Olaf College",      590, 710      , 590, 710,
"Salisbury University",    540, 620      , 540, 610,
"Samford University",      510, 630      , 520, 630,
"Santa Clara University",  610, 700      , 590, 680,
"Scripps College", 620, 700      , 640, 730,
"Seattle University",      540, 640      , 530, 640,
"Seton Hall University",   510, 610      , 490, 590,
"Sewanee University",      580, 660      , 590, 690,
"Siena College",   510, 610      , 490, 590,
"Simmons College", 520, 620      , 520, 630,
"Skidmore College",        570, 670      , 560, 680,
"Smith College",   600, 710      , 610, 720,
"Sonoma State University", 450, 560      , 440, 550,
"Southern Methodist University",   620, 700      , 600, 690,
"Southwestern University", 540, 640      , 520, 640,
"Spelman College", 460, 540      , 470, 570,
"St. Bonaventure University",      470, 600      , 460, 580,
"St. John's University",   490, 620      , 480, 590,
"St. Lawrence University", 570, 660      , 550, 650,
"St. Mary's College of Maryland",  540, 650      , 570, 670,
"Stanford University",     700, 790      , 680, 780,
"Stephens College",        440, 540      , 480, 590,
"Stevens Institute of Technology", 630, 670      , 540, 670,
"Suffolk University",      450, 570      , 440, 560,
"SUNY at Albany",  520, 610      , 490, 580,
"SUNY at Binghamton",      630, 710      , 590, 680,
"SUNY at Buffalo", 550, 650      , 500, 600,
"SUNY at Stony Brook",     600, 700      , 550, 650,
"SUNY College at Geneseo", 600, 700      , 580, 690,
"SUNY Purchase College",   480, 580      , 500, 600,
"Susquehanna University",  510, 610      , 510, 620,
"Swarthmore College",      670, 770      , 680, 780,
"Sweet Briar College",     450, 570      , 490, 610,
"Syracuse University",     540, 650      , 500, 620,
"Temple University",       510, 620      , 500, 610,
"Texas A&M University",    520, 610      , 500, 590,
"Texas Christian University",      550, 650      , 540, 620,
"The Catholic University of America",      510, 610      , 500, 610,
"The College of New Jersey",       580, 680      , 550, 660,
"The College of Wooster",  540, 660      , 540, 660,
"The Evergreen State College",     450, 580      , 500, 630,
"The George Washington University",        600, 700      , 600, 690,
"The University of Alabama",       500, 640      , 500, 620,
"The University of Scranton",      530, 620      , 510, 600,
"The University of South Dakota",  460, 620      , 430, 640,
"The University of Texas at Austin",       580, 710      , 550, 670,
"The University of Tulsa", 570, 690      , 560, 710,
"Transylvania University", 520, 620      , 520, 660,
"Trinity College", 600, 700      , 590, 690,
"Trinity University",      580, 670      , 570, 680,
"Truman State University", 540, 680      , 540, 680,
"Tufts University",        690, 770      , 680, 750,
"Tulane University",       620, 700      , 620, 700,
"Union College",   620, 700      , 590, 680,
"United States Air Force Academy", 620, 710      , 590, 690,
"United States Coast Guard Academy",       620, 690      , 570, 670,
"United States Merchant Marine Academy",   610, 690      , 570, 660,
"United States Military Academy",  600, 690      , 580, 700,
"University of Arizona",   490, 620      , 480, 600,
"University of Arkansas",  520, 630      , 500, 610,
"University of California-Berkeley",       650, 770      , 600, 730,
"University of California-Davis",  570, 690      , 520, 640,
"University of California-Los Angeles",    600, 760      , 560, 680,
"University of California-Riverside",      500, 630      , 470, 580,
"University of California-San Diego",      560, 720      , 510, 650,
"University of California-Santa Barbara",  570, 690      , 540, 660,
"University of California-Santa Cruz",     490, 630      , 470, 610,
"University of Central Florida",   550, 650      , 530, 630,
"University of Chicago",   710, 790      , 710, 780,
"University of Colorado",  540, 650, 520, 630,
"University of Connecticut",       580, 680      , 550, 650,
"University of Dallas",    530, 640      , 550, 670,
"University of Dayton",    500, 640      , 510, 620,
"University of Delaware",  560, 660      , 540, 650,
"University of Denver",    560, 660      , 550, 640,
"University of Florida",   590, 690      , 580, 670,
"University of Georgia",   580, 670      , 560, 660,
"University of Hawaii",    500, 610, 480, 580,
"University of Idaho",     490, 600      , 480, 590,
"University of Illinois",  680, 790, 550, 680,
"University of Iowa",      550, 690      , 470, 630,
"University of Kentucky",  510, 630      , 500, 620,
"University of Maine",     480, 600      , 470, 590,
"University of Mary Washington",   510, 600      , 520, 630,
"University of Maryland",  610, 720      , 580, 690,
"University of Massachusetts",     560, 660      , 530, 630,
"University of Miami",     630, 720      , 600, 700,
"University of Michigan",  650, 760      , 610, 700,
"University of Minnesota", 620, 740      , 550, 690,
"University of Mississippi",       480, 600      , 480, 600,
"University of Missouri",  530, 650      , 510, 640,
"University of Montana",   470, 600      , 480, 600,
"University of Nebraska",  520, 670      , 490, 660,
"University of New Hampshire",     500, 610      , 490, 590,
"University of New Mexico",        470, 600      , 470, 610,
"University of New Orleans",       490, 620      , 470, 590,
"University of North Carolina",    610, 710      , 590, 690,
"University of Notre Dame",        680, 770      , 660, 750,
"University of Oklahoma",  540, 660      , 510, 640,
"University of Oregon",    500, 620      , 490, 600,
"University of Pennsylvania",      690, 780      , 660, 760,
"University of Pittsburgh",        600, 680      , 570, 660,
"University of Puget Sound",       580, 660      , 570, 690,
"University of Redlands",  520, 620      , 510, 610,
"University of Rhode Island",      510, 620      , 490, 590,
"University of Richmond",  620, 720      , 580, 700,
"University of Rochester", 650, 750      , 600, 700,
"University of San Diego", 570, 670      , 540, 650,
"University of San Francisco",     530, 630      , 510, 620,
"University of South Carolina",    560, 650      , 540, 640,
"University of South Florida",     540, 640      , 530, 630,
"University of Southern California",       650, 760      , 620, 720,
"University of Tennessee", 520, 650, 520, 640,
"University of the Pacific",       550, 690      , 520, 650,
"University of Utah",      510, 650      , 510, 620,
"University of Vermont",   540, 650      , 540, 640,
"University of Virginia",  640, 740      , 620, 720,
"University of Washington",        580, 700      , 520, 650,
"University of Wisconsin", 630, 750      , 530, 650,
"University of Wyoming",   500, 630      , 480, 610,
"Ursinus College", 540, 660      , 540, 650,
"Valparaiso University",   510, 620      , 500, 590,
"Vanderbilt University",   710, 790      , 690, 770,
"Vassar College",  650, 730      , 660, 750,
"Villanova University",    610, 710      , 590, 680,
"Wabash College",  530, 640      , 500, 610,
"Wagner College",  530, 630      , 520, 640,
"Wake Forest University",  630, 710      , 620, 700,
"Warren Wilson College",   480, 590      , 510, 660,
"Washington and Lee University",   650, 740      , 650, 740,
"Washington State University",     470, 600      , 460, 570,
"Wellesley College",       640, 740      , 650, 740,
"Wells College",   470, 590      , 480, 600,
"Wesleyan College",        420, 540      , 450, 580,
"Wesleyan University",     660, 740      , 640, 740,
"West Virginia University",        470, 580      , 460, 560,
"Westminster College",     490, 600, 470, 590,
"Whitman College", 610, 690      , 610, 730,
"Whittier College",        480, 590      , 470, 580,
"Willamette University",   540, 650      , 540, 660,
"William Jewell College",  510, 610      , 530, 600,
"Williams College",        660, 770      , 670, 770,
"Wittenberg University",   500, 620      , 500, 620,
"Wofford College", 590, 680      , 570, 630,
"Worcester Polytechnic Institute", 640, 720      , 560, 670,
"Xavier University",       510, 610      , 500, 600,
"Yale University", 710, 790      , 700, 800,
]
class C:
    def __init__(self, name, lm, hm, lr, hr):
        from Range import Range
        self.name = name
        self.math_range = Range(lm, hm)
        self.read_range = Range(lr, hr)
    def printC(self):
        print "{0} Math {1}-{2} Reading {3}-{4}".format(self.name, self.math_range.bottom,
              self.math_range.top, self.read_range.bottom, self.read_range.top)

def get_sizes():
    colleges = []
    url = "http://collegestats.org/colleges/all/largest/%d/"
    page = 1
    colls = []
    while page < 3:
        url = "http://collegestats.org/colleges/all/largest/%d/" % (page)
        request = urllib2.urlopen(url)
        soup = BeautifulSoup(request.read())
        div = soup.find(id="content")
        names = []
        sizes = []
        tuitions = []
        addresses = []
        num = 0
        tuition_num = 0
        address_num = 0
        for td in div.find_all('td'):
            try:
                if td['class'][0] == "state":
                    print td.string
                    if address_num < 3:
                        address_num += 1
                        continue
                    address = "adr213, zip0143"
                    for meta in td.find_all('meta'):
                        if meta['itemprop'] == "streetAddress":
                            address = address.replace("adr213", meta['content'])
                        if meta['itemprop'] == "postalCode":
                            address = address.replace("zip0143", meta['content'])
                    addresses.append(address)
                if td['class'][0] == "name":
                    if num < 3:
                        num += 1
                        continue
                    name = td.a.string.strip()
                    names.append(name)
                if td['class'][0] == "students":
                    size = int(td.string.replace(",",""))
                    sizes.append(size)
                if td['class'][0] == "tuition":
                    if tuition_num < 3:
                        tuition_num += 1
                        continue
                    if "N/A" in td.string:
                        tuition = 0
                    else:
                        tuition = int(td.string.replace(",","").replace("$",""))
                    tuitions.append(tuition)
            except:
                continue
        #l = [ (x, y, z) for x in names for y in sizes for z in tuitions ]
        l = zip(names, sizes, tuitions, addresses)
        page += 1
        colls.append(l)
    colls = [item for sublist in colls for item in sublist]
    return colls




def populate_database():
    """
        Returns a list of College objects to be stored in the database
        Then they can be reconstructed by called
        colleges = db_load_colleges()
    """
    database_schools = []
    n = 0
    cols = []
    cols_with_size = get_sizes()
    while n < len(colleges_with_sat):
        c = C(colleges_with_sat[n], colleges_with_sat[n+1], colleges_with_sat[n+2], colleges_with_sat[n+3], colleges_with_sat[n+4])
        cols.append(c)
        n+=5
                
    for i in range(0, len(colleges)):
        if False: #db_college_exists(name):
            continue
        name = colleges[i]
        sats = {}
        size = 0
        tuition = 0
        address = ""
        matched = False
        for c in cols:
            if levenshtein(c.name, name) < 4:
                matched = True
                sats['math'] = c.math_range
                sats['reading'] = c.read_range
        if not matched:
            sats = None
        for c in cols_with_size:
            if levenshtein(c[0], name) < 4:
                self.size = c[1]
                self.tuition = c[2]
                self.address = c[3]
                break
        college = College(name, "", i, sats, size, tuition, address)
        database_schools.append(college)
        college.print_college()
        user = User()
        user.name = "Aaron"
        user.sats = {"math" : 800, "reading" : 800}
        print college.find_location()
        #print college.get_difficulty()
    return database_schools
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
print get_sizes()
#populate_database()
#
#user = User()
#user.name = "Aaron"
#i = 400
#while i <= 800:
#    user.sats = {"math" : i, "reading" : i}
#    print "Math: %d Reading: %d Level: %f" % (user.sats['math'], user.sats['reading'],
#            user.get_level())
#    i += 10
