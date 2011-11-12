##########################################################################
#  
#  Copyright (c) 2011, John Haddon. All rights reserved.
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#  
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#  
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
##########################################################################

import unittest

import IECore

import Gaffer
import GafferUI

class TabbedContainerTest( unittest.TestCase ) :
	
	def test( self ) :
	
		t = GafferUI.TabbedContainer()
		self.assertEqual( len( t ), 0 )
		
		self.assertEqual( t.getCurrent(), None )
		
		c = GafferUI.ListContainer( GafferUI.ListContainer.Orientation.Vertical )
		
		t.append( c )
		self.assertEqual( len( t ), 1 )
		self.assert_( t[0] is c )
		self.assert_( t.getCurrent() is c )
		
	def testOwner( self ) :
	
		t = GafferUI.TabbedContainer()
		
		self.failUnless( GafferUI.Widget._owner( t._qtWidget() ) is t )
	
	def testCornerWidget( self ) :
	
		t = GafferUI.TabbedContainer()
		self.failUnless( t.getCornerWidget() is None )
		
		b = GafferUI.Button( "baby" )
		t.setCornerWidget( b )
		self.failUnless( t.getCornerWidget() is b )
		self.failUnless( b.parent() is t )
		
		b2 = GafferUI.Button( "b" )
		t.setCornerWidget( b2 )
		self.failUnless( t.getCornerWidget() is b2 )
		self.failUnless( b2.parent() is t )
		self.failUnless( b.parent() is None )
		
if __name__ == "__main__":
	unittest.main()
	
