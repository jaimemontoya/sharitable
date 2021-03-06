#!"C:\Python27\python.exe"
#modeled from https://github.com/pgbovine/csc210-fall-2015/blob/master/www/cgi-bin/lecture4-create-database.py

import sqlite3

#database called users.db
conn = sqlite3.connect('donors.db')
c = conn.cursor()

#varchar is a variable length character string
#making a table called 'users' inside donors.db
c.execute('create table users(username varchar(10) primary key, password varchar(20), address varchar(100), zipcode int)')

#filling in db with users (maybe not do for real)
c.execute("insert into users values('stargirl27', 'elephant360!', '500 Joseph C. Wilson Blvd, Rochester, NY', 14627);")
c.execute("insert into users values('emichel2', 'password', '500 Joseph C. Wilson Blvd, Rochester, NY', 14086);")
c.execute("insert into users values('fish99', 'iheartbob6*', '500 Joseph C. Wilson Blvd, Rochester, NY', 14225);")
c.execute("insert into users values('bobram8', '92798@!', '500 Joseph C. Wilson Blvd, Rochester, NY', 14043);")
c.execute("insert into users values('cow', 'moo', '87 Brooks Ave, Rochester, NY', 14225);")



#table for items called 'items' inside donors.db
#note: no primary key because allowing multiple entries with the same username. 
#c.execute('create table items(username varchar(10), type varchar(30), subtype varchar(30), quantity int)')

#filling in with a few items
#c.execute("insert into items values('stargirl27','clothing','jeans',5);")
#c.execute("insert into items values('emichel2','clothing','coats',2);")
#c.execute("insert into items values('fish99','appliances','mixer',1);")
#c.execute("insert into items values('bobram8','clothing','shoes',3);")
#c.execute("insert into items values('stargirl27','toys','dress-up clothes',1);")
#c.execute("insert into items values('bobram8','furniture','couch',1);")

# Creating a table called 'item'. 
c.execute('CREATE TABLE item(itemid integer primary key, itemname varchar(30), itemtypeid integer)')
# Populating the table 'item'
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (1, "Shirt", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (2, "Pants", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES(3, "Shoes", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (4, "Bed", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (5, "Table", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (6, "Desk", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (7, "Board game", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (8, "Video game", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (9, "Doll", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (10, "Jacket", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (11, "Chair", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (12, "Legos", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (13, "Dress", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (14, "Sofa", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (15, "Train set", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (16, "Suit", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (17, "Crib", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (18, "Stuffed Animals", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (19, "Snow Boots", 1)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (20, "Island", 2)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (21, "Playing Cards", 3)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (22, "Refrigerator", 4)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (23, "Microwave", 4)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (24, "Lawn Mower", 4)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (25, "Snow Blower", 4)')
c.execute('INSERT INTO item(itemid, itemname, itemtypeid) VALUES (26, "Tool Set", 4)')



# Creating a table called 'type'
c.execute('CREATE TABLE type(typeid integer primary key, typename varchar(20))')
# Populating the table 'type'
c.execute('INSERT INTO type(typeid, typename) VALUES (1, "Clothes")')
c.execute('INSERT INTO type(typeid, typename) VALUES (2, "Furniture")')
c.execute('INSERT INTO type(typeid, typename) VALUES (3, "Toys")')
c.execute('INSERT INTO type(typeid, typename) VALUES (4, "Appliances or Tools")')

# Creating a table called 'user_donation'
c.execute('CREATE TABLE user_donation(user_donationsid integer primary key autoincrement, username varchar(10), itemid integer, description varchar(100), quantity integer, timestamp not null default current_timestamp)')

# Creating a table called 'organization'
c.execute('CREATE TABLE organization(organizationid integer primary key, organizationname varchar(30), zipcode integer, photo varchar(30), site varchar(100), address varchar(100))') #note: photo is name only!

c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (1,"Goodwill", 14627, "goodwill.jpg", "http://www.goodwill.org/", "120 Mount Hope Avenue, Rochester, NY ")')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (2,"Ronald McDonald House", 14620, "ronaldmcdonald.jpg", "http://www.rmhc.org/", "333 Westmoreland Dr., Rochester, NY")')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (3,"Hilliside Family of Agencies", 14611, "hillside.jpg", "https://www.hillside.com/","89 Genesee St, Rochester, NY")')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (4,"Foodlink Food Bank", 14615, "foodlink.jpg", "http://foodlinkny.org/","1999 Mt. Read Blvd")')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (5,"Amvets", 14043, "amvets.jpg" , "http://amvetsnsf.org/thrift-stores/", "2900 Walden Avenue, Depew, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (6,"Caring Hands for Angels", 14627, "caring.png" , "http://caringhandsforangels.com/", "" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (7,"CASA", 14614, "blank.png" , "http://www.CASARochester.org", "99 Exchange Boulevard, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (8,"Center for Youth", 14620, "cfy.jpg" , "http://www.centerforyouth.net/", "905 Monroe Avenue, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (9,"Children Awaiting Parents", 14607, "cap.jpg" , "http://www.childrenawaitingparents.org/", "274 N. Goodman St., Rochester, NY " )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (10,"Families in Recovery", 14609, "blank.png" , "http://www.FamiliesInRecovery.org", "1115 East Main Street, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (11,"Make a Wish", 14618, "maw.jpg" , "http://www.WNY.Wish.org/", "1855 Monroe Avenue, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (12,"Open School of Rochester", 14619, "blank.png" , "http://OpenSchool.RocUS.org", "261 Winbourne Rd, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (13,"Pirate Toy Fund", 14609, "ptf.png" , "http://www.PirateToyFund.org", "1453 East Main Street Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (14,"Rochester Childfirst Network", 14620, "rcn.png" , "http://rcn4kids.org/", "941 South Avenue, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (15,"Sojourner House", 14619, "sjh.jpg" , "http://www.SojournerHouse.org", "30 Millbank Street, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (16,"Twelve Corners Day Care", 14623, "tcd.png" , "http://www.TwelveCornersDayCare.com", "155 Canal View Boulevard, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (17,"Webster Montessori School", 14580, "wms.jpg" , "http://www.WebsterMontessori.org", "1310 Five Mile Line Road, Webster, NY " )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (18,"19th Ward Community Association", 14619, "19wc.png" , "http://www.19wca.org", "216 Thurston Road, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (19,"Community Place of Greater Rochester", 14605, "cpr.png" , "http://www.CommunityPlace.org", "57 Central Park, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (20,"M.K. Gandhi Institute for Nonviolence", 14608, "blank.png" , "http://www.GandhiInstitute.org", "929 South Plymouth Avenue, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (21,"Rochester AmeriCorps", 14604, "acr.gif" , "http://www.RochesterAmeriCorps.org/", "228 East Main Street, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (22,"Pathstone", 14607, "path.jpg" , "http://PathStone.org", "400 East Avenue, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (23,"AIDS Rochester", 14043, "blank.png" , "http://www.AIDSRochester.org", "1350 University Avenue, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (24,"East House", 14607, "ehroc.jpg" , "http://www.EastHouse.org", "259 Monroe Avenue, Suite 200, Rochester NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (25,"His Branches, Inc.", 14627, "hisbran.jpg" , "http://www.hisbranches.org/", "342 Arnett Boulevard, Rochester, NY" )')
#not real- but shows an organization that does not have a website. 
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (26,"Clothes 4 U", 14611, "blank.png" , "An organization run by the Jones family that donates clothes to the homeless in Rochester. Call 585-555-5555 for more information.", "36 Spruce Avenue, Rochester, NY" )')
c.execute('INSERT INTO organization(organizationid, organizationname, zipcode, photo, site, address) VALUES (27,"Catholic Charities", 14212, "blank.png" , "http://www.ccwny.org/", "491 Emslie St, Buffalo, NY" )')


#key of item id's 
#1, "Shirt" #2, "Pants"#3, "Shoes" #4, "Bed" #5, "Table" #6, "Desk" #7, "Board game" #8, "Video game" #9, "Doll"

# Creating a table called 'item_organization'
#gen_id is similar to user_donationsid in user_donation table
c.execute('CREATE TABLE item_organization(gen_id integer primary key autoincrement, org_id integer, org_itemid integer)')
#filling in for now
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (1,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (1,2)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (1,3)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (2,4)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (2,7)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (3,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (5,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (6,7)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (7,3)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (7,5)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (8,9)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (10,4)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (9,2)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (12,5)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (11,4)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (13,9)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (15,8)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (14,6)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (18,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (16,4)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (17,7)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (20,7)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (22,8)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (21,3)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (24,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (23,3)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (24,5)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (25,5)')

c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (26,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (26,2)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (26,3)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (26,19)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (27,1)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (27,2)')
c.execute('INSERT INTO item_organization(org_id, org_itemid) VALUES (27,3)')
#**how specific do we want this to be? subtypes or types? or combination? 

conn.commit()
conn.close()
