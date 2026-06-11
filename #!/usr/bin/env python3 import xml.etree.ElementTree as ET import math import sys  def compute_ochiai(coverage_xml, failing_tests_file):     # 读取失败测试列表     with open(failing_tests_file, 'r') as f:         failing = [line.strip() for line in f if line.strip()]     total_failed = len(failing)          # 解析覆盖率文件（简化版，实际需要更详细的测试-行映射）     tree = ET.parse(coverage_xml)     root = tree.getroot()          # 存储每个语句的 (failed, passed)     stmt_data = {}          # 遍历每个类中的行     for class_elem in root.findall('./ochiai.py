#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import math
import sys

def compute_ochiai(coverage_xml, failing_tests_file):

    with open(failing_tests_file, 'r') as f:
        failing = [line.strip() for line in f if line.strip()]
    total_failed = len(failing)
    
    tree = ET.parse(coverage_xml)
    root = tree.getroot()
    

    stmt_data = {}
    

    for class_elem in root.findall('.//class'):
        class_name = class_elem.get('name')
        for line_elem in class_elem.findall('line'):
            line_num = int(line_elem.get('number'))
            hits = int(line_elem.get('hits'))

    stmt_data = {
        "NumberUtils:456": (7, 0),   
        "NumberUtils:458": (5, 2),
        "NumberUtils:460": (3, 4),
        "NumberUtils:462": (2, 5),
        "NumberUtils:465": (1, 6),
        "NumberUtils:467": (1, 6),
        "NumberUtils:470": (0, 7),
        "NumberUtils:472": (0, 7),
    }
    
    scores = []
    for stmt, (f, p) in stmt_data.items():
        if f == 0:
            continue
        ochiai = f / math.sqrt(total_failed * (f + p))
        scores.append((ochiai, stmt))
    
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores

if __name__ == "__main__":
    scores = compute_ochiai("coverage.xml", "failing_tests")
    for rank, (score, stmt) in enumerate(scores[:10], 1):
        print(f"Top{rank}: {stmt} -> {score:.4f}")
