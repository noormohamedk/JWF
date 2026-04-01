from pathlib import Path
p = Path('jwf.html')
t = p.read_text(encoding='utf-8')
start = t.find('<div class="projects-grid">')
if start == -1:
    print('start not found');
    raise SystemExit(1)
end = t.find('<!-- ===== EVENTS ===== -->', start)
if end == -1:
    print('end not found');
    raise SystemExit(1)

new = '''    <div class="projects-grid">
      <div class="project-card reveal">
        <div class="project-img">
          <img src="file:///E:/web page/poster/10 X 8 copy.jpg" alt="Education & Scholarship Support" />
        </div>
        <div class="project-body">
          <span class="project-tag">Education</span>
          <h3>Education & Scholarship Support</h3>
          <p>Comprehensive scholarships and mentorship which empower rural students through academic support and school refurbishment.</p>
          <a href="featured-projects/education-scholarship-support.html" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="project-card reveal reveal-delay-1">
        <div class="project-img">
          <img src="file:///E:/web page/poster/10X8 ramazan welcome copy.jpg" alt="Youth Empowerment Initiatives" />
        </div>
        <div class="project-body">
          <span class="project-tag">Youth</span>
          <h3>Youth Empowerment Initiatives</h3>
          <p>Mentorship programs, training and civic engagement activities for young community members.</p>
          <a href="featured-projects/youth-empowerment-initiatives.html" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="project-card reveal reveal-delay-2">
        <div class="project-img">
          <img src="file:///E:/web page/poster/3 x 2 amp copy.jpg" alt="Community Health Programs" />
        </div>
        <div class="project-body">
          <span class="project-tag">Health</span>
          <h3>Community Health Programs</h3>
          <p>Health camps, maternal and child healthcare, and clean water access in remote regions.</p>
          <a href="featured-projects/community-health-programs.html" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="project-card reveal">
        <div class="project-img">
          <img src="file:///E:/web page/poster/ramalan kit copy.jpg" alt="Social Impact Research" />
        </div>
        <div class="project-body">
          <span class="project-tag">Research</span>
          <h3>Social Impact Research</h3>
          <p>Evidence-based analysis and policy reports driving community impact.</p>
          <a href="featured-projects/social-impact-research.html" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="project-card reveal reveal-delay-1">
        <div class="project-img">
          <img src="file:///E:/web page/poster/10x8 seminar class 1.jpg" alt="Humanitarian Relief" />
        </div>
        <div class="project-body">
          <span class="project-tag">Relief</span>
          <h3>Humanitarian Relief</h3>
          <p>Rapid-response aid with food, shelter, and medical services for crisis-affected communities.</p>
          <a href="featured-projects/humanitarian-relief.html" class="project-link">View Details <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>
'''

out = t[:start] + new + '\n<!-- ===== EVENTS ===== -->' + t[end+len('<!-- ===== EVENTS ===== -->'):]
p.write_text(out, encoding='utf-8')
print('done')
