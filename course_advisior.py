###   Name: Nwankwo Chukwuebuka Justin
###   Date: 1/27/2016
###   Last Updated: 8/27/2016



def get_file_contents(fp, filetype, degree_plan = {}):
    if(filetype.lower() == 'degree_plan'):
        for line in fp:
            line_split = line.split(',')

            course = line_split[0].strip()
            title = line_split[1].strip()
            prerequisite = line_split[2].split('|')


            prerequisite =  [val.strip() for val in prerequisite]
           
                

            degree_plan[course] = {'course_title': title,
                                   'prerequisite': prerequisite,
                                   'course_taken': 0,
                                   'credit_hour':'NA',
                                   'grade':'NA'
                                  }
        return degree_plan

    else:
        if (not len(degree_plan.keys())):
            return
        
        for line in fp:
            line_split = line.strip().split(',')
            course = line_split[0].strip()
            credit_hr = line_split[1]
            grade = line_split[2]

            degree_plan[course]['course_taken'] = 1
            degree_plan[course]['credit_hour'] = credit_hr
            degree_plan[course]['grade'] = grade
            
        return degree_plan
        

    

    

### to optimize use topological sort to get eligible courses
def get_eligible_courses(courses_left, degree_plan):

  eligible_courses = []

      
  for course in courses_left:
      prereq = degree_plan[course]['prerequisite']
      index = courses_left.index(course)
      
          
      if(len(prereq) == 0):
          if(course not in eligible_courses):
              eligible_courses.append(course)
              continue

      if(prereq[0][0] == '*'):
          eligible_courses.append(course)
          continue

      isFound = False
      for val in prereq:
          if(not degree_plan[val]['course_taken']):
              isFound = True
              break

      

      if(not isFound and course not in eligible_courses):
          eligible_courses.append(course)
        


  return eligible_courses
          
          


    
def display_courses(courses, degree_plan):
    for course in courses:
        print course, ' --> ', degree_plan[course]['course_title']
      

            







#filename = raw_input("Enter degree plan file name: ")
degree_file = 'comp_eng_degree_plan.csv'
course_file = 'courses_taken.txt'

dfp = open(degree_file,'r')
cfp = open(course_file,'r')
    

degree_plan = get_file_contents(dfp, 'degree_plan')
dfp.close()


courses_taken = get_file_contents(cfp, 'courses_taken')
cfp.close()


courses_left = []

for course in degree_plan:
    if (not degree_plan[course]['course_taken']):
        courses_left.append(course)

                                                               



print "Courses left to take: "
print '-'*40
display_courses(courses_left, degree_plan)
print
print 
eligible_courses = get_eligible_courses(courses_left[:], degree_plan)

print "Courses eligible to take: "
print '-'*40
display_courses(eligible_courses,degree_plan)


    
