import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_get_courses_html(self):
        
            courseOne = ['Math', 'English', 'History']
            #test for get course html
            self.assertEqual(get_courses_html(courseOne), '<div><h3>Courses</h3><span>Math, English, History</span></div>')

            courseTwo = ['Basketball', 'Soccer', 'Skydive']
            #test for get course html
            self.assertEqual(get_courses_html(courseTwo), '<div><h3>Courses</h3><span>Basketball, Soccer, Skydive</span></div>')


            courseThree = ['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering']
            #test for get course html
            self.assertEqual(get_courses_html(courseThree), '<div><h3>Courses</h3><span>Programming Languages and Techniques, Biomedical image analysis, Software Engineering</span></div>')

    def test_get_projects_html(self):
    
        projectOne = ['Java Spring', 'Spring MVC', 'Designed a complete website using React']
        #test for get projectOne html
        self.assertEqual(get_projects_html(projectOne), '<div><h2>Projects</h2><ul><li>Java Spring</li><li>Spring MVC</li><li>Designed a complete website using React</li></ul></div>')
  
        projectTwo = ['Create Rocket', 'Create aircraft', 'Designed computer']
        #test for get projectTwo html
        self.assertEqual(get_projects_html(projectTwo), '<div><h2>Projects</h2><ul><li>Create Rocket</li><li>Create aircraft</li><li>Designed computer</li></ul></div>')

    def test_get_info_html(self):
    
        #test for get info html
        self.assertEqual(get_info_html('Yiting', 'yitingchen@gmail.com'), '<div><h1>Yiting</h1><p>yitingchen@gmail.com</p></div>')

        #test for get info html
        self.assertEqual(get_info_html('David', 'davidgch@gmail.com'), '<div><h1>David</h1><p>davidgch@gmail.com</p></div>')

        #test for get info html
        self.assertEqual(get_info_html('Lucy', 'lucyCat@gmail.com'), '<div><h1>Lucy</h1><p>lucyCat@gmail.com</p></div>')

    def test_get_courses(self):
        
        #test for get courses for any random punctuation
        self.assertListEqual(get_courses(['Lucy', 'Courses++++++++ :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Math', 'English', 'History'])

        #test for get courses for leading or trailing whitespace
        self.assertListEqual(get_courses(['Lucy', 'Courses :-   Math  ,    English   ,    History  ', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Math', 'English', 'History'])


    def test_get_projects(self):
    
        #test for get projects
        self.assertListEqual(get_projects(['Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Java Spring', 'Spring MVC', 'Designed a complete website using React'])
        
        #test for get projects for leading or trailing whitespace
        self.assertListEqual(get_projects(['Yiting', 'Courses :- Math, English, History', 'Projects    ', '   Java Spring   ', '   Spring MVC   ',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Java Spring', 'Spring MVC', 'Designed a complete website using React'])
        
    def test_get_name(self):

        #test for invalid name because of number
        self.assertEqual(get_name(['  25Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Invalid name')

        #test for invalid name because of lowercase letter
        self.assertEqual(get_name(['lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Invalid name')

        ##test for the correct name
        self.assertEqual(get_name(['Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Lucy')

    def test_get_email(self):
        
        #test for invalid email
        self.assertEqual(get_email(['Yiting', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.org']), '')

        #test for invalid email
        self.assertEqual(get_email(['Yiting', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@25seas.upenn.org']), '')

        #test for invalid email
        self.assertEqual(get_email(['Lucy (name lowercase)', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'yiting@seas.upenn.edu')


if __name__ == '__main__':
    unittest.main()
