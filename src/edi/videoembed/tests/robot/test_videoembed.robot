# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.videoembed -t test_videoembed.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.videoembed.testing.EDI_VIDEOEMBED_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_videoembed.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Videoembed
  Given a logged-in site administrator
    and an add videoembed form
   When I type 'My Videoembed' into the title field
    and I submit the form
   Then a videoembed with the title 'My Videoembed' has been created

Scenario: As a site administrator I can view a Videoembed
  Given a logged-in site administrator
    and a videoembed 'My Videoembed'
   When I go to the videoembed view
   Then I can see the videoembed title 'My Videoembed'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add videoembed form
  Go To  ${PLONE_URL}/++add++Videoembed

a videoembed 'My Videoembed'
  Create content  type=Videoembed  id=my-videoembed  title=My Videoembed


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the videoembed view
  Go To  ${PLONE_URL}/my-videoembed
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a videoembed with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the videoembed title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
