﻿<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Example" Type="Folder">
			<Item Name="example 3" Type="Folder">
				<Item Name="example 3 - subpanel.vi" Type="VI" URL="../examples/example 3 - subpanel.vi"/>
				<Item Name="example 3 - subpanel1.vi" Type="VI" URL="../examples/example 3 - subpanel1.vi"/>
				<Item Name="example 3 - subpanel2.vi" Type="VI" URL="../examples/example 3 - subpanel2.vi"/>
			</Item>
			<Item Name="example 4b" Type="Folder">
				<Item Name="example 4b - child.vi" Type="VI" URL="../examples/example 4b - child.vi"/>
				<Item Name="example 4b - grand child.vi" Type="VI" URL="../examples/example 4b - grand child.vi"/>
				<Item Name="example 4b - string.vi" Type="VI" URL="../examples/example 4b - string.vi"/>
			</Item>
			<Item Name="example 5" Type="Folder">
				<Item Name="example 5 - child.vi" Type="VI" URL="../ui-testing/example 5 - child.vi"/>
				<Item Name="example 5 - grand child.vi" Type="VI" URL="../ui-testing/example 5 - grand child.vi"/>
				<Item Name="example 5 - parent.vi" Type="VI" URL="../ui-testing/example 5 - parent.vi"/>
			</Item>
			<Item Name="example 6" Type="Folder">
				<Item Name="example 6 - child.vi" Type="VI" URL="../ui-testing/example 6 - child.vi"/>
				<Item Name="example 6 - grand child.vi" Type="VI" URL="../ui-testing/example 6 - grand child.vi"/>
				<Item Name="example 6 - visibility.vi" Type="VI" URL="../ui-testing/example 6 - visibility.vi"/>
			</Item>
			<Item Name="example 7" Type="Folder">
				<Item Name="example 7 - child.vi" Type="VI" URL="../ui-testing/example 7 - child.vi"/>
				<Item Name="example 7 - cluster.vi" Type="VI" URL="../ui-testing/example 7 - cluster.vi"/>
				<Item Name="example 7 - grand child.vi" Type="VI" URL="../ui-testing/example 7 - grand child.vi"/>
			</Item>
			<Item Name="example 8" Type="Folder">
				<Item Name="example 8 - child.vi" Type="VI" URL="../ui-testing/example 8 - child.vi"/>
				<Item Name="example 8 - grand child.vi" Type="VI" URL="../ui-testing/example 8 - grand child.vi"/>
				<Item Name="example 8 - mouse click.vi" Type="VI" URL="../examples/example 8 - mouse click.vi"/>
			</Item>
			<Item Name="example 9" Type="Folder">
				<Item Name="example 9 - bool.vi" Type="VI" URL="../ui-testing/example 9 - bool.vi"/>
				<Item Name="example 9 - child.vi" Type="VI" URL="../ui-testing/example 9 - child.vi"/>
				<Item Name="example 9 - grand child.vi" Type="VI" URL="../ui-testing/example 9 - grand child.vi"/>
			</Item>
			<Item Name="example 1 - plot.vi" Type="VI" URL="../examples/example 1 - plot.vi"/>
			<Item Name="example 2 - value.vi" Type="VI" URL="../examples/example 2 - value.vi"/>
			<Item Name="example 4 - string.vi" Type="VI" URL="../examples/example 4 - string.vi"/>
			<Item Name="example 10 - resolve data.vi" Type="VI" URL="../ui-testing/example 10 - resolve data.vi"/>
		</Item>
		<Item Name="Tests" Type="Folder">
			<Item Name="test - all.vi" Type="VI" URL="../ui-testing/test - all.vi"/>
		</Item>
		<Item Name="utils" Type="Folder">
			<Item Name="MGI backup" Type="Folder">
				<Item Name="Anything to String - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/Anything to String - backup.vi"/>
				<Item Name="Build Line - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/Build Line - backup.vi"/>
				<Item Name="Get Cluster Elements - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/Get Cluster Elements - backup.vi"/>
				<Item Name="MGI Get VI Control Ref[] - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/MGI Get VI Control Ref[] - backup.vi"/>
				<Item Name="Process Array Elements - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/Process Array Elements - backup.vi"/>
				<Item Name="Replace Characters - backup.vi" Type="VI" URL="../ui-testing/MGI - backup/Replace Characters - backup.vi"/>
			</Item>
		</Item>
		<Item Name="ui-testing.lvlib" Type="Library" URL="../ui-testing/ui-testing.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="ClassID Names Enum__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/ClassID Names Enum__ogtk.ctl"/>
				<Item Name="Current VIs Parents Ref__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/Current VIs Parents Ref__ogtk.vi"/>
				<Item Name="Find Focus State__ogtk.ctl" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/Find Focus State__ogtk.ctl"/>
				<Item Name="Find VI with Focus__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/Find VI with Focus__ogtk.vi"/>
				<Item Name="Fit VI window to Largest Dec__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/Fit VI window to Largest Dec__ogtk.vi"/>
				<Item Name="Is One Frontmost__ogtk.vi" Type="VI" URL="/&lt;userlib&gt;/_OpenG.lib/appcontrol/appcontrol.llb/Is One Frontmost__ogtk.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVNumericRepresentation.ctl" Type="VI" URL="/&lt;vilib&gt;/numeric/LVNumericRepresentation.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_Data Type.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/Data Type/NI_Data Type.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="TRef Traverse.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/traverseref.llb/TRef Traverse.vi"/>
				<Item Name="TRef TravTarget.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/traverseref.llb/TRef TravTarget.ctl"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="UTF8 Tools.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/Tools/Unicode/UTF8 Tools.lvlib"/>
				<Item Name="VariantType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/VariantDataType/VariantType.lvlib"/>
				<Item Name="VI Scripting - Traverse.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/traverseref.llb/VI Scripting - Traverse.lvlib"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="zeromq.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/zeromq/zeromq.lvlib"/>
			</Item>
			<Item Name="User32.dll" Type="Document" URL="User32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="test" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{FBE69F21-2A88-4137-BFF1-4494A5482989}</Property>
				<Property Name="App_INI_GUID" Type="Str">{AC4E741B-5E78-4E48-B5F3-110760B4C88C}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{DC60D93B-5E7D-436D-A338-89E52375BAEB}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">test</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/test</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{6FC5B723-7B03-47F5-8A25-2BF65D79ABF3}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">test.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/test/test.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/test/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{BE09DDAA-B9DA-475D-8DA5-4E2EB02230DC}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Dependencies/Items in Memory/main.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">FLUXiM AG</Property>
				<Property Name="TgtF_fileDescription" Type="Str">test</Property>
				<Property Name="TgtF_internalName" Type="Str">test</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2024 FLUXiM AG</Property>
				<Property Name="TgtF_productName" Type="Str">test</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{93DC929D-039A-497F-B87C-80A8F5A1DBD8}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">test.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
