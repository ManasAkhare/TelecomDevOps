import os
import zipfile

def create_pptx(filename, slides_data):
    # XML templates
    content_types_header = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
'''
    content_types_footer = '</Types>'

    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>'''

    pres_rels_header = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
'''
    pres_rels_footer = '</Relationships>'

    theme = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="DevOps Theme">
  <a:themeElements>
    <a:clrScheme name="DevOps">
      <a:dk1><a:sysClr val="windowText" lastClr="0F172A"/></a:dk1>
      <a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1E293B"/></a:dk2>
      <a:lt2><a:srgbClr val="F8FAFC"/></a:lt2>
      <a:accent1><a:srgbClr val="2563EB"/></a:accent1>
      <a:accent2><a:srgbClr val="06B6D4"/></a:accent2>
      <a:accent3><a:srgbClr val="10B981"/></a:accent3>
      <a:accent4><a:srgbClr val="F59E0B"/></a:accent4>
      <a:accent5><a:srgbClr val="EF4444"/></a:accent5>
      <a:accent6><a:srgbClr val="8B5CF6"/></a:accent6>
      <a:hlink><a:srgbClr val="3B82F6"/></a:hlink>
      <a:folHlink><a:srgbClr val="6366F1"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Office">
      <a:majorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>
      <a:minorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Office">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
</a:theme>'''

    master_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>'''

    master = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><p:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></p:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>'''

    layout_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>'''

    layout = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><p:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></p:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sldLayout>'''

    slide_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>'''

    num_slides = len(slides_data)

    content_types_items = []
    pres_rels_items = []
    pres_sld_ids = []

    for i in range(1, num_slides + 1):
        content_types_items.append(f'  <Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>')
        pres_rels_items.append(f'  <Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>')
        pres_sld_ids.append(f'    <p:sldId id="{255 + i}" r:id="rId{i+1}"/>')

    content_types = content_types_header + "\n".join(content_types_items) + "\n" + content_types_footer
    pres_rels = pres_rels_header + "\n".join(pres_rels_items) + "\n" + pres_rels_footer

    pres = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>
{chr(10).join(pres_sld_ids)}
  </p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>'''

    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('[Content_Types].xml', content_types)
        zf.writestr('_rels/.rels', rels)
        zf.writestr('ppt/_rels/presentation.xml.rels', pres_rels)
        zf.writestr('ppt/presentation.xml', pres)
        zf.writestr('ppt/theme/theme1.xml', theme)
        zf.writestr('ppt/slideMasters/_rels/slideMaster1.xml.rels', master_rels)
        zf.writestr('ppt/slideMasters/slideMaster1.xml', master)
        zf.writestr('ppt/slideLayouts/_rels/slideLayout1.xml.rels', layout_rels)
        zf.writestr('ppt/slideLayouts/slideLayout1.xml', layout)

        for i, s in enumerate(slides_data, start=1):
            zf.writestr(f'ppt/slides/_rels/slide{i}.xml.rels', slide_rels)
            
            # Generate shapes for this slide
            # Shape 1: Header/Title Banner
            # Shape 2: Body text / bullets / cards
            title = s.get('title', '')
            subtitle = s.get('subtitle', '')
            bullets = s.get('bullets', [])
            cards = s.get('cards', [])

            # Slide XML builder
            sp_xml = []
            
            # Slide Background shape (Dark obsidian #0B1120)
            sp_xml.append('''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Bg"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="0" y="0"/><a:ext cx="12192000" cy="6858000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="0B1120"/></a:solidFill>
          <a:ln><a:noFill/></a:ln>
        </p:spPr>
      </p:sp>''')

            # Top Accent Line
            sp_xml.append('''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="AccentLine"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="600000" y="400000"/><a:ext cx="10992000" cy="40000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="06B6D4"/></a:solidFill>
        </p:spPr>
      </p:sp>''')

            # Title Box
            safe_title = title.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            safe_sub = subtitle.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            sp_xml.append(f'''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="TitleBox"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="600000" y="550000"/><a:ext cx="10992000" cy="1100000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/><a:lstStyle/>
          <a:p><a:r><a:rPr lang="en-US" sz="3200" b="1"><a:solidFill><a:srgbClr val="F8FAFC"/></a:solidFill></a:rPr><a:t>{safe_title}</a:t></a:r></a:p>
          <a:p><a:r><a:rPr lang="en-US" sz="1600"><a:solidFill><a:srgbClr val="94A3B8"/></a:solidFill></a:rPr><a:t>{safe_sub}</a:t></a:r></a:p>
        </p:txBody>
      </p:sp>''')

            # Cards or Bullets Layout
            if cards:
                card_width = int(10992000 / len(cards)) - 150000
                for c_idx, c in enumerate(cards):
                    c_x = 600000 + c_idx * (card_width + 150000)
                    c_title = c.get('title', '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    c_text = c.get('text', '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    c_val = c.get('highlight', '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    
                    sp_xml.append(f'''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="{10 + c_idx*2}" name="CardBg{c_idx}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{c_x}" y="1900000"/><a:ext cx="{card_width}" cy="4200000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 3000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="1E293B"/></a:solidFill>
          <a:ln w="12700"><a:solidFill><a:srgbClr val="334155"/></a:solidFill></a:ln>
        </p:spPr>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="{11 + c_idx*2}" name="CardTxt{c_idx}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{c_x + 150000}" y="2050000"/><a:ext cx="{card_width - 300000}" cy="3900000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/><a:lstStyle/>
          <a:p><a:r><a:rPr lang="en-US" sz="2000" b="1"><a:solidFill><a:srgbClr val="38BDF8"/></a:solidFill></a:rPr><a:t>{c_title}</a:t></a:r></a:p>
          <a:p><a:r><a:rPr lang="en-US" sz="2800" b="1"><a:solidFill><a:srgbClr val="10B981"/></a:solidFill></a:rPr><a:t>{c_val}</a:t></a:r></a:p>
          <a:p><a:pPr><a:buNone/></a:pPr><a:r><a:rPr lang="en-US" sz="1400"><a:solidFill><a:srgbClr val="CBD5E1"/></a:solidFill></a:rPr><a:t>{c_text}</a:t></a:r></a:p>
        </p:txBody>
      </p:sp>''')

            elif bullets:
                bullet_xml = []
                for b in bullets:
                    safe_b = b.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    bullet_xml.append(f'''
          <a:p>
            <a:pPr marL="288000" indent="-288000"><a:buFont typeface="Arial"/><a:buChar char="▪"/></a:pPr>
            <a:r><a:rPr lang="en-US" sz="1600"><a:solidFill><a:srgbClr val="E2E8F0"/></a:solidFill></a:rPr><a:t>{safe_b}</a:t></a:r>
          </a:p>''')

                sp_xml.append(f'''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="20" name="BulletsCard"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="600000" y="1900000"/><a:ext cx="10992000" cy="4200000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 2000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="131D31"/></a:solidFill>
          <a:ln w="12700"><a:solidFill><a:srgbClr val="334155"/></a:solidFill></a:ln>
        </p:spPr>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="21" name="BulletsContent"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="900000" y="2100000"/><a:ext cx="10392000" cy="3800000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/><a:lstStyle/>
{''.join(bullet_xml)}
        </p:txBody>
      </p:sp>''')

            # Footer / Candidate Info
            sp_xml.append(f'''
      <p:sp>
        <p:nvSpPr><p:cNvPr id="30" name="Footer"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="600000" y="6300000"/><a:ext cx="10992000" cy="350000"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/><a:lstStyle/>
          <a:p>
            <a:r><a:rPr lang="en-US" sz="1100"><a:solidFill><a:srgbClr val="64748B"/></a:solidFill></a:rPr><a:t>Candidate: Manas Akhare (Roll: 23102C0017) | BE - VII (Div C, Sr. 12) | Ansible Telecom Outage Dashboard | Slide {i} of {num_slides}</a:t></a:r>
          </a:p>
        </p:txBody>
      </p:sp>''')

            slide_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><p:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></p:xfrm></p:grpSpPr>
{''.join(sp_xml)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sld>'''
            zf.writestr(f'ppt/slides/slide{i}.xml', slide_xml)

    print(f"SUCCESS: Created {filename} with {num_slides} slides ({os.path.getsize(filename):,} bytes)")

if __name__ == '__main__':
    sample_slides = [
        {
            'title': 'Ansible-Provisioned Telecom Service Outage Dashboard',
            'subtitle': 'Enterprise-Grade DevOps Pipeline & Observability Platform',
            'cards': [
                {'title': 'Candidate Details', 'highlight': 'Manas Akhare', 'text': 'Roll No: 23102C0017\nClass: BE - VII (Div C, Sr. 12)\nAcademic Year: 2026-27 ODD Sem'},
                {'title': 'Technology Stack', 'highlight': 'Full-Stack DevOps', 'text': 'Java 17, Spring Boot 3.2.5, H2\nDocker, Jenkins, Ansible\nSelenium, MockMvc, JUnit 5'},
                {'title': 'Deployment State', 'highlight': '100% Passing', 'text': '15/15 Automated Tests OK\nPort 8085 Verified\nIdempotent Ansible IaC'}
            ]
        },
        {
            'title': 'Problem Statement & DevOps Motivation',
            'subtitle': 'Eliminating Operational Fragility in Mission-Critical Telecom Infrastructure',
            'bullets': [
                'Telecom service downtime costs $10,000 to $50,000 per minute with severe regulatory penalties and customer churn.',
                'Traditional operational silos cause slow incident detection, manual configuration drift, and high MTTR.',
                'Manual deployments risk configuration discrepancies across staging and production nodes.',
                'Solution: Build a real-time reactive outage dashboard with automated CI/CD and immutable Ansible orchestration.'
            ]
        }
    ]
    create_pptx('test_presentation.pptx', sample_slides)
