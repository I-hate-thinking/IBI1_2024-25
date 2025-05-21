import xml.dom.minidom
import xml.sax
from datetime import datetime
from collections import defaultdict

# DOM Approach
def dom_analysis(xml_file):
    start_time = datetime.now()
    
    # Parse the XML file
    dom = xml.dom.minidom.parse(xml_file)
    
    # Initialize dictionaries to store max depth terms for each namespace
    max_depth_terms = {
        'molecular_function': {'term_id': None, 'depth': -1},
        'biological_process': {'term_id': None, 'depth': -1},
        'cellular_component': {'term_id': None, 'depth': -1}
    }
    
    # Get all term elements
    terms = dom.getElementsByTagName('term')
    
    for term in terms:
        # Get namespace
        namespace_elements = term.getElementsByTagName('namespace')
        if not namespace_elements:
            continue
        namespace = namespace_elements[0].firstChild.nodeValue
        
        # Only process the three main ontologies
        if namespace not in max_depth_terms:
            continue
        
        # Get term ID
        term_id_elements = term.getElementsByTagName('id')
        if not term_id_elements:
            continue
        term_id = term_id_elements[0].firstChild.nodeValue
        
        # Count is_a relationships
        is_a_elements = term.getElementsByTagName('is_a')
        depth = len(is_a_elements)
        
        # Update max depth if current term is deeper
        if depth > max_depth_terms[namespace]['depth']:
            max_depth_terms[namespace]['term_id'] = term_id
            max_depth_terms[namespace]['depth'] = depth
    
    end_time = datetime.now()
    processing_time = end_time - start_time
    
    return max_depth_terms, processing_time

# SAX Approach
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ''
        self.term_id = ''
        self.namespace = ''
        self.is_a_count = 0
        self.max_depth_terms = {
            'molecular_function': {'term_id': None, 'depth': -1},
            'biological_process': {'term_id': None, 'depth': -1},
            'cellular_component': {'term_id': None, 'depth': -1}
        }
    
    def startElement(self, name, attrs):
        self.current_element = name
        if name == 'term':
            self.term_id = ''
            self.namespace = ''
            self.is_a_count = 0
    
    def characters(self, content):
        if self.current_element == 'id':
            self.term_id += content.strip()
        elif self.current_element == 'namespace':
            self.namespace += content.strip()
    
    def endElement(self, name):
        if name == 'is_a':
            self.is_a_count += 1
        elif name == 'term':
            if self.namespace in self.max_depth_terms:
                if self.is_a_count > self.max_depth_terms[self.namespace]['depth']:
                    self.max_depth_terms[self.namespace]['term_id'] = self.term_id
                    self.max_depth_terms[self.namespace]['depth'] = self.is_a_count
            self.current_element = ''

def sax_analysis(xml_file):
    start_time = datetime.now()
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    
    end_time = datetime.now()
    processing_time = end_time - start_time
    
    return handler.max_depth_terms, processing_time

def main():
    xml_file = '/Users/dongfeiyang/Desktop/IBI1_2024-25/Practical14/go_obo.xml'
    
    # DOM analysis
    print("Running DOM analysis...")
    dom_results, dom_time = dom_analysis(xml_file)
    print("\nDOM Results:")
    for namespace, data in dom_results.items():
        print(f"{namespace}: Term {data['term_id']} with depth {data['depth']}")
    print(f"DOM Processing Time: {dom_time}")
    
    # SAX analysis
    print("\nRunning SAX analysis...")
    sax_results, sax_time = sax_analysis(xml_file)
    print("\nSAX Results:")
    for namespace, data in sax_results.items():
        print(f"{namespace}: Term {data['term_id']} with depth {data['depth']}")
    print(f"SAX Processing Time: {sax_time}")
    
    # Compare results and performance
    print("\nComparison:")
    print(f"DOM and SAX produced the same results: {dom_results == sax_results}")
    print(f"SAX was {'faster' if sax_time < dom_time else 'slower'} than DOM")

if __name__ == '__main__':
    main()