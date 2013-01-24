##########################################################################
#  
#  Copyright (c) 2012, John Haddon. All rights reserved.
#  Copyright (c) 2013, Image Engine Design Inc. All rights reserved.
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

class TransformPlugTest( unittest.TestCase ) :

	def testMatrix( self ) :
	
		p = Gaffer.TransformPlug()
		
		p["translate"].setValue( IECore.V3f( 1, 2, 3 ) )
		p["rotate"].setValue( IECore.V3f( 90, 45, 0 ) )
		p["scale"].setValue( IECore.V3f( 1, 2, 4 ) )
		
		translate = IECore.M44f.createTranslated( p["translate"].getValue() )
		rotate = IECore.Eulerf( IECore.degreesToRadians( p["rotate"].getValue() ), IECore.Eulerf.Order.XYZ, IECore.Eulerf.InputLayout.XYZLayout )
		rotate = rotate.toMatrix44()
		scale = IECore.M44f.createScaled( p["scale"].getValue() )
		transforms = {
			"t" : translate,
			"r" : rotate,
			"s" : scale,
		}
		transform = IECore.M44f()
		for m in ( "trs" ) :
			transform = transform * transforms[m]

		self.assertEqual( p.matrix(), transform )
	
	def testCreateCounterpart( self ) :
	
		t = Gaffer.TransformPlug()
		t2 = t.createCounterpart( "a", Gaffer.Plug.Direction.Out )
		
		self.assertEqual( t2.getName(), "a" )
		self.assertEqual( t2.direction(), Gaffer.Plug.Direction.Out )
		self.assertTrue( isinstance( t2, Gaffer.TransformPlug ) )
		
	def testRunTimeTyped( self ) :
	
		p = Gaffer.TransformPlug()
		self.failIf( p.typeId() == Gaffer.CompoundPlug.staticTypeId() )
		self.failUnless( p.isInstanceOf( Gaffer.CompoundPlug.staticTypeId() ) )

if __name__ == "__main__":
	unittest.main()
	
