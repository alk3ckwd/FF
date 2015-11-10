from django.db import models

# Create your models here.
class games(models.Model):
	week = models.IntegerField(default=0)
	home_team = models.ForeignKey('stats', related_name='home_team')
	away_team = models.ForeignKey('stats', related_name='away_team')
	venue_type = models.CharField(max_length=100, blank=True, null=True)
	venue_surface = models.CharField(max_length=100, blank=True, null=True)

	def as_dict(self):
		return {
			"week": self.week,
			"home_team": self.home_team,
			"away_team": self.away_team,
			"venue_type": self.venue_type,
			"venue_surface": self.venue_surface
		}

	def __str__(self):
		return "%s vs. %s" % self.home_team, self.away_team


class stats(models.Model):
	
	off_sl_pct = models.IntegerField(default=0)
	off_sm_pct = models.IntegerField(default=0)
	off_sr_pct = models.IntegerField(default=0)
	off_ll_pct = models.IntegerField(default=0)
	off_lm_pct = models.IntegerField(default=0)
	off_lr_pct = models.IntegerField(default=0)
	def_sl_pct = models.IntegerField(default=0)
	def_sm_pct = models.IntegerField(default=0)
	def_sr_pct = models.IntegerField(default=0)
	def_ll_pct = models.IntegerField(default=0)
	def_lm_pct = models.IntegerField(default=0)
	def_lr_pct = models.IntegerField(default=0)
	team_name = models.CharField(max_length=5)

	def as_dict(self):
		return {
			"team_name": self.team_name,
			"off_sl": self.off_sl_pct,
			"off_sm": self.off_sm_pct,
			"off_sr": self.off_sr_pct,
			"off_ll": self.off_ll_pct,
			"off_lm": self.off_lm_pct,
			"off_lr": self.off_lr_pct,
			"def_sl": self.def_sl_pct,
			"def_sm": self.def_sm_pct,
			"def_sr": self.def_sr_pct,
			"def_ll": self.def_ll_pct,
			"def_lm": self.def_lm_pct,
			"def_lr": self.def_lr_pct
		}

class targets(models.Model):
	target_team_name = models.ForeignKey('stats', related_name='target_team_name')
	deep_left = models.CharField(max_length=100)
	deep_middle = models.CharField(max_length=100)
	deep_right = models.CharField(max_length=100)
	short_left = models.CharField(max_length=100)
	short_middle = models.CharField(max_length=100)
	short_right = models.CharField(max_length=100)






