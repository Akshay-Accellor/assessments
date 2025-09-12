Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-16: Structured URLs for Landing Pages', () => {
    before(async () => { await browser.url('http://www.ipsy.com/admin/campaign-create'); });
    it('Positive - Verify structured URLs for campaigns are generated correctly', async () => {
        const campaignForm = await $('.campaign-form');
        await expect(campaignForm).toBeDisplayed();
        const identifierInput = await $('.identifier');
        await identifierInput.setValue('campaign-id');
        const save = await $('.save-campaign');
        await save.click();
        const urlDisplay = await $('.url-display');
        await expect(urlDisplay).toHaveTextContaining('/campaign-id');
        await browser.url(urlDisplay.getText());
        const page = await $('body');
        await expect(page).toBeDisplayed();
    });
    it('Negative - Verify failure with invalid identifier', async () => {
        const identifierInput = await $('.identifier');
        await identifierInput.setValue('invalid@id');
        const save = await $('.save-campaign');
        await save.click();
        const errorMessage = await $('.error-message');
        await expect(errorMessage).toBeDisplayed();
    });
    it('Edge - Verify with long identifier', async () => {
        const identifierInput = await $('.identifier');
        await identifierInput.setValue('a'.repeat(100));
        const save = await $('.save-campaign');
        await save.click();
        const urlDisplay = await $('.url-display');
        await expect(urlDisplay).toBeDisplayed();
    });
});
