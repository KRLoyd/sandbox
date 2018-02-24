from mongoengine import *

# connect to database 'tumblelog'
connect('tumblelog')

class User(Document):
    '''
    User document schema for User collection

    * Never passed to MongoDB - only enforced on application level
    makes future changes easier to manage
    '''
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Post(Document):
    '''
    Post document schema for Post collection

    is the base for all posts
    '''
    title = StringField(max_length=120, required=True)
    
    ##
    # ReferenceField
    #
    # Similar to Foreign Keys in ORMs
    # Automatically translated into references when saved ad dereferenced when loaded
    # Handle deletion rules: keyword reverse_delete_rule
    ##
    author = ReferenceField(User, reverse_delete_rule=CASCADE)

    ##
    # ListField
    # takes a field object as 1st parameter
    ## 
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocument(Comment))

    meta = {'allow_inheritance': True}

class TextPost(Post):
    '''
    TextPost document schema
    
    Inherits from Post
    '''
    content = StringField()

class ImagePost(Post):
    '''
    ImagePost document schema

    Inherits from Post
    '''
    image_path = StringField()

class LinkPost(Post):
    '''
    LinkPost document schema

    Inherits from Post
    '''
    link_url = StringField()

class Comment(EmbeddedDocument):
    '''
    Comment document to be embedded directly to a Post document

    Treat no different than a regular document
    Does not have it's oun collection in the database
    '''
    content = StringField()
    name = StringField(max_length=120)

##
# Add data to the database
##
ross = User(email='ross@example.com', first_name='Ross', last_name='Lawlwy').save()
john = User(email='john@ex.com', first_name='John', last_name='Doe').save()

post1 = TextPost(title='Fun with MongoEngine', author=john)
post1.content = 'Took a look at MongoEngine today. Looks cool!'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='MongoEngine Documentation', author=ross)
post2.link_url = 'http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()

##
# Display data in database
#
# Each document has an objects attribute. 
# Used to access the documents in the database collection associated with the class
##
for post in Post.objects:
    print(post.title)

##
# Retrieve type-specific info
##
for post in TextPost.objects:
    print(post.content)

for post in Post.objects:
    print(post.title)
    print('=' * len(post.title))

    if isinstance(post, TextPost):
        print(post.content)
    
    if isinstance(post, LinkPost):
        print('Link: {}'.format(post.link_url))

##
# Search for posts by tag
##
for post in Post.objects(tags='mongodb'):
    print(post.title)

num_posts = Post.objects(tags='mongodb').count()
print('Found {} posts with the tag "mongodb"'.format(num_posts))